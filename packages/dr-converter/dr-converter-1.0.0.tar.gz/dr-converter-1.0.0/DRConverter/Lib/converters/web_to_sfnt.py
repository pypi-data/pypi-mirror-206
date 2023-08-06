import time

from PyQt6.QtCore import QRunnable, pyqtSlot, QObject, pyqtSignal
from fontTools.misc.cliTools import makeOutputFileName

from DRConverter.Lib.converters.options import WebToSFNTOptions
from DRConverter.Lib.font.Font import Font


class WorkerSignals(QObject):
    progress = pyqtSignal(str)
    finished = pyqtSignal()


class JobRunner_wf2ft(QRunnable):
    def __init__(self, files):
        super().__init__()
        self.files = files
        self.options = WebToSFNTOptions()
        self.signals = WorkerSignals()
        self.is_killed = False

    @pyqtSlot()
    def run(self) -> None:
        count = 0
        for file in self.files:
            t = time.time()
            count += 1
            self.signals.progress.emit(f"\nConverting file {count} of {len(self.files)}: {file}")
            try:
                font = Font(file, recalcTimestamp=self.options.recalc_timestamp)

                if not font.flavor:
                    continue
                if not self.options.woff:
                    if font.flavor == "woff":
                        continue
                if not self.options.woff2:
                    if font.flavor == "woff2":
                        continue

                old_extension = font.get_real_extension()
                if self.options.woff and self.options.woff2:
                    suffix = old_extension
                else:
                    suffix = ""
                font.flavor = None
                new_extension = font.get_real_extension()
                output_file = makeOutputFileName(
                    file,
                    extension=new_extension,
                    suffix=suffix,
                    outputDir=self.options.output_dir,
                    overWrite=self.options.overwrite,
                )

                font.save(output_file)
                message = f"{output_file} saved\nElapsed time: {round(time.time() - t, 3)} seconds"

            except Exception as e:
                message = f"FAIL: {e}"

            if self.is_killed:
                break

            self.signals.progress.emit(message)

        self.signals.finished.emit()
