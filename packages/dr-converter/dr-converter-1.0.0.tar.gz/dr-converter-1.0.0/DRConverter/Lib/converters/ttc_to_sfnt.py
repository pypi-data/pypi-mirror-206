import time

from PyQt6.QtCore import QObject, pyqtSignal, QRunnable
from fontTools.misc.cliTools import makeOutputFileName
from fontTools.ttLib import TTCollection

from DRConverter.Lib.converters.options import TTCollectionToSFNTOptions


class WorkerSignals(QObject):
    progress = pyqtSignal(str)
    finished = pyqtSignal()


class JobRunner_ttc2sfnt(QRunnable):
    def __init__(self, files):
        super().__init__()
        self.files = files
        self.options = TTCollectionToSFNTOptions()
        self.signals = WorkerSignals()
        self.is_killed = False

    def run(self) -> None:
        count = 0
        for file in self.files:
            count += 1
            t = time.time()

            self.signals.progress.emit(f"\nConverting file {count} of {len(self.files)}: {file}")

            try:
                ttc = TTCollection(file)
                for font in ttc.fonts:
                    font.recalcTimestamp = self.options.recalc_timestamp
                    file_name = font["name"].getDebugName(6)
                    extension = ".otf" if font.sfntVersion == "OTTO" else ".ttf"
                    output_file = makeOutputFileName(
                        file_name,
                        outputDir=self.options.output_dir,
                        extension=extension,
                        overWrite=self.options.overwrite,
                    )
                    font.save(output_file)
                    self.signals.progress.emit(f"{output_file} saved")

                self.signals.progress.emit(f"{len(ttc.fonts)} fonts saved in {round(time.time() - t, 3)} seconds")

            except Exception as e:
                message = f"FAIL: {e}"
                self.signals.progress.emit(message)

            if self.is_killed:
                break

        self.signals.finished.emit()
