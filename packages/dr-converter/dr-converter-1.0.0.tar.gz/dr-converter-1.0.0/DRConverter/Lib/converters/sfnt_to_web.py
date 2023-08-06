import time

from PyQt6.QtCore import QObject, pyqtSignal, QRunnable
from fontTools.misc.cliTools import makeOutputFileName

from DRConverter.Lib.font.Font import Font
from DRConverter.Lib.converters.options import SFNTToWebOptions


class WorkerSignals(QObject):
    progress = pyqtSignal(str)
    finished = pyqtSignal()


class JobRunner_ft2wf(QRunnable):
    def __init__(self, files):
        super().__init__()
        self.files = files
        self.options = SFNTToWebOptions()
        self.signals = WorkerSignals()
        self.is_killed = False

    def run(self) -> None:
        output_flavors = ["woff", "woff2"]
        if not self.options.woff:
            output_flavors.remove("woff")
        if not self.options.woff2:
            output_flavors.remove("woff2")

        count = 0
        for file in self.files:
            t = time.time()
            count += 1
            self.signals.progress.emit(f"\nConverting file {count} of {len(self.files)}: {file}")
            try:
                font = Font(file, recalcTimestamp=self.options.recalc_timestamp)

                if font.flavor is not None:
                    continue

                if self.options.woff:
                    converter = SFNTToWeb(font=font, flavor="woff")
                    web_font = converter.run()
                    extension = web_font.get_real_extension()
                    output_file = makeOutputFileName(
                        file, extension=extension, outputDir=self.options.output_dir, overWrite=self.options.overwrite
                    )
                    web_font.save(output_file, reorderTables=False)
                    message = f"{output_file} saved\nElapsed time: {round(time.time() - t, 3)} seconds"
                    self.signals.progress.emit(message)

                if self.options.woff2:
                    converter = SFNTToWeb(font=font, flavor="woff2")
                    web_font = converter.run()
                    extension = web_font.get_real_extension()
                    output_file = makeOutputFileName(
                        file, extension=extension, outputDir=self.options.output_dir, overWrite=self.options.overwrite
                    )
                    web_font.save(output_file, reorderTables=False)
                    message = f"{output_file} saved\nElapsed time: {round(time.time() - t, 3)} seconds"
                    self.signals.progress.emit(message)

            except Exception as e:
                message = f"FAIL: {e}"
                self.signals.progress.emit(message)

            if self.is_killed:
                break

        self.signals.finished.emit()


class SFNTToWeb(object):
    def __init__(self, font: Font, flavor: str):
        self.font = font
        self.flavor = flavor

    def run(self) -> Font:
        self.font.flavor = self.flavor
        return self.font
