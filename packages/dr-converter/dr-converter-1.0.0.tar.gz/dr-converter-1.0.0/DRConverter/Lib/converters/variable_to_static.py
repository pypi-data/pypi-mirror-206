import time

from PyQt6.QtCore import QObject, pyqtSignal, QRunnable
from fontTools.misc.cliTools import makeOutputFileName
from fontTools.varLib.instancer import instantiateVariableFont, OverlapMode
from pathvalidate import sanitize_filename

from DRConverter.Lib.converters.options import Var2StaticOptions
from DRConverter.Lib.font.VFont import VariableFont


class WorkerSignals(QObject):
    progress = pyqtSignal(str)
    finished = pyqtSignal()


class JobRunner_vf2i(QRunnable):
    def __init__(self, files):
        super().__init__()
        self.files = files
        self.options = Var2StaticOptions()
        self.signals = WorkerSignals()
        self.is_killed = False

    def run(self) -> None:
        count = 0
        for file in self.files:
            count += 1
            self.signals.progress.emit(f"\nConverting file {count} of {len(self.files)}: {file}")

            try:
                variable_font = VariableFont(file, recalcTimestamp=self.options.recalc_timestamp)
                instances = variable_font.get_instances()
                if len(instances) == 0:
                    self.signals.progress.emit(f"ERROR: no static instances found.")
                    break

                if self.options.update_name_table:
                    if "STAT" not in variable_font:
                        self.options.update_name_table = False
                        self.signals.progress.emit("WARNING: Cannot update name table if there is no STAT table.")
                    if not hasattr(variable_font["STAT"], "AxisValueArray"):
                        self.options.update_name_table = False
                        self.signals.progress.emit(
                            "WARNING: Cannot update name table if there are no STAT Axis Values."
                        )

                instance_count = 0
                for instance in instances:
                    t = time.time()
                    instance_count += 1
                    self.signals.progress.emit(f"\nExporting instance {instance_count} of {len(instances)}")

                    try:
                        static_instance = instantiateVariableFont(
                            varfont=variable_font,
                            axisLimits=instance.coordinates,
                            inplace=False,
                            overlap=OverlapMode.REMOVE_AND_IGNORE_ERRORS,
                            optimize=True,
                            updateFontNames=self.options.update_name_table,
                        )

                        if "cvar" in static_instance:
                            del static_instance["cvar"]

                        if self.options.cleanup:
                            name_ids_to_delete = (
                                variable_font.get_var_name_ids_to_delete() if self.options.cleanup else []
                            )
                            static_instance.name_table.del_names(name_ids=name_ids_to_delete)

                            if "STAT" in static_instance:
                                del static_instance["STAT"]

                            static_instance.reorder_ui_name_ids()

                        static_instance_name = sanitize_filename(variable_font.get_instance_file_name(instance))
                        static_instance_extension = static_instance.get_real_extension()
                        output_file = makeOutputFileName(
                            static_instance_name,
                            extension=static_instance_extension,
                            outputDir=self.options.output_dir,
                            overWrite=self.options.overwrite,
                        )
                        static_instance.save(output_file)
                        message = f"{output_file} saved\nElapsed time: {round(time.time() - t, 3)} seconds"

                    except Exception as e:
                        message = f"FAIL: {e}"

                    self.signals.progress.emit(message)

                    if self.is_killed:
                        break

            except Exception as e:
                message = f"FAIL: {e}"
                self.signals.progress.emit(message)

        self.signals.finished.emit()
