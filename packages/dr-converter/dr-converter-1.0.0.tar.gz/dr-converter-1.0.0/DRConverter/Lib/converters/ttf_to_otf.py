import time

from afdko import checkoutlinesufo
from cffsubr import subroutinize
import pathops
from PyQt6.QtCore import QRunnable, QObject, pyqtSignal
from fontTools.fontBuilder import FontBuilder
from fontTools.misc.cliTools import makeOutputFileName
from fontTools.pens.qu2cuPen import Qu2CuPen
from fontTools.pens.t2CharStringPen import T2CharStringPen
from DRConverter.Lib.utils.subsetter import BaseSubsetter

from DRConverter.Lib.font.Font import Font
from DRConverter.Lib.converters.options import TrueTypeToCFFOptions


class WorkerSignals(QObject):
    progress = pyqtSignal(str)
    finished = pyqtSignal()


class JobRunner_ttf2otf(QRunnable):
    def __init__(self, files):
        super().__init__()
        self.files = files
        self.options = TrueTypeToCFFOptions()
        self.signals = WorkerSignals()
        self.is_killed = False

    def run(self) -> None:
        count = 0
        for file in self.files:
            t = time.time()
            count += 1

            try:
                self.signals.progress.emit(f"\nConverting file {count} of {len(self.files)}: {file}")

                source_font = Font(file, recalcTimestamp=self.options.recalc_timestamp)

                # Set tolerance as a ratio of unitsPerEm
                tolerance = self.options.tolerance / 1000 * source_font["head"].unitsPerEm

                ext = ".otf" if source_font.flavor is None else source_font.get_real_extension()
                suffix = "" if source_font.flavor is None else ".otf"
                output_file = makeOutputFileName(
                    file,
                    suffix=suffix,
                    extension=ext,
                    outputDir=self.options.output_dir,
                    overWrite=self.options.overwrite,
                )

                if self.options.safe_mode:
                    # Create a temporary OTF file with T2CharStringPen...
                    from DRConverter.Lib.converters.otf_to_ttf import CFFToTrueType

                    ttf2otf_converter_temp = TrueTypeToCFF(source_font)
                    ttf2otf_converter_temp.options.charstring_source = "t2"
                    ttf2otf_converter_temp.options.subroutinize = False
                    ttf2otf_converter_temp.options.purge_glyphs = self.options.remove_glyphs
                    temp_cff_font = ttf2otf_converter_temp.run()

                    # ... and convert it back to a temporary TTF file that will be used for conversion
                    otf_to_ttf_converter = CFFToTrueType(temp_cff_font)
                    # since the temp CFF font has many more points than needed, increase max_err from 1.0 to 2.0
                    otf_to_ttf_converter.options.max_err = 2.0
                    input_font = otf_to_ttf_converter.run()

                else:
                    input_font = source_font

                if self.options.scale_upm:
                    from fontTools.ttLib.scaleUpem import scale_upem

                    scale_upem(input_font, 1000)

                ttf2otf_converter = TrueTypeToCFF(font=input_font)
                ttf2otf_converter.options.charstring_source = "qu2cu"
                ttf2otf_converter.options.tolerance = tolerance
                ttf2otf_converter.options.subroutinize = self.options.subroutinize
                ttf2otf_converter.options.purge_glyphs = self.options.remove_glyphs
                ttf2otf_converter.options.check_outlines = self.options.check_outlines
                cff_font = ttf2otf_converter.run()

                cff_font.save(output_file)

                if self.options.check_outlines:
                    self.signals.progress.emit("Checking outlines with checkoutlinesufo")
                    checkoutlinesufo.run(args=[output_file, "--error-correction-mode", "--quiet-mode"])

                message = f"{output_file} saved\nElapsed time: {round(time.time() - t, 3)} seconds"

            except Exception as e:
                message = f"FAIL: {e}"

            self.signals.progress.emit(message)

            if self.is_killed:
                break

        self.signals.finished.emit()


class TrueTypeToCFF(object):
    def __init__(self, font: Font):
        self.font = font
        self.options = TrueTypeToCFFOptions()

    def run(self):
        if self.options.remove_glyphs:
            self.purge_glyphs()

        charstrings = {}

        if self.options.charstring_source == "qu2cu":
            self.font.decomponentize()
            try:
                charstrings = self.get_qu2cu_charstrings(tolerance=self.options.tolerance, all_cubic=True)
            except NotImplementedError:
                try:
                    charstrings = self.get_qu2cu_charstrings(tolerance=self.options.tolerance, all_cubic=False)
                except:
                    return

        if self.options.charstring_source == "t2":
            try:
                charstrings = self.get_t2_charstrings()
            except:
                return

        cff_font_info = self.get_cff_font_info()
        post_values = self.get_post_values()

        fb = FontBuilder(font=self.font)
        fb.isTTF = False
        for table in ["glyf", "cvt ", "loca", "fpgm", "prep", "gasp", "LTSH", "hdmx"]:
            if table in fb.font:
                del fb.font[table]

        fb.setupCFF(
            psName=self.font.name_table.getDebugName(6),
            charStringsDict=charstrings,
            fontInfo=cff_font_info,
            privateDict={},
        )
        fb.setupDummyDSIG()
        fb.setupMaxp()
        fb.setupPost(**post_values)

        if self.options.subroutinize:
            # cffsubr doesn't work with woff/woff2 fonts
            flavor = fb.font.flavor
            if flavor is not None:
                fb.font.flavor = None
            subroutinize(fb.font)
            fb.font.flavor = flavor

        return fb.font

    def get_cff_font_info(self) -> dict:
        """
        Setup CFF topDict

        :return: A dictionary of the font info.
        """

        font_revision = str(round(self.font["head"].fontRevision, 3)).split(".")
        major_version = str(font_revision[0])
        minor_version = str(font_revision[1]).ljust(3, "0")

        cff_font_info = dict(
            version=".".join([major_version, str(int(minor_version))]),
            FullName=self.font.name_table.getBestFullName(),
            FamilyName=self.font.name_table.getBestFamilyName(),
            ItalicAngle=self.font["post"].italicAngle,
            UnderlinePosition=self.font["post"].underlinePosition,
            UnderlineThickness=self.font["post"].underlineThickness,
            isFixedPitch=False if self.font["post"].isFixedPitch == 0 else True,
        )

        return cff_font_info

    def get_post_values(self) -> dict:
        post_info = dict(
            italicAngle=round(self.font["post"].italicAngle),
            underlinePosition=self.font["post"].underlinePosition,
            underlineThickness=self.font["post"].underlineThickness,
            isFixedPitch=self.font["post"].isFixedPitch,
            minMemType42=self.font["post"].minMemType42,
            maxMemType42=self.font["post"].maxMemType42,
            minMemType1=self.font["post"].minMemType1,
            maxMemType1=self.font["post"].maxMemType1,
        )
        return post_info

    def purge_glyphs(self):
        glyph_ids_to_remove = []
        for g in [".null", "NUL", "NULL", "uni0000", "CR", "nonmarkingreturn", "uni000D"]:
            try:
                glyph_ids_to_remove.append(self.font.getGlyphID(g))
            except KeyError:
                pass

        glyph_ids = [i for i in self.font.getReverseGlyphMap().values() if i not in glyph_ids_to_remove]
        if len(glyph_ids_to_remove) > 0:
            subsetter = BaseSubsetter(glyph_ids=glyph_ids)
            subsetter.subset(self.font)

    def get_qu2cu_charstrings(self, tolerance: float = 1, all_cubic: bool = True):
        charstrings = {}
        glyph_set = self.font.getGlyphSet()

        for k, v in glyph_set.items():
            # Correct contours direction and remove overlaps with pathops
            pathops_path = pathops.Path()
            pathops_pen = pathops_path.getPen(glyphSet=glyph_set)
            try:
                glyph_set[k].draw(pathops_pen)
                pathops_path.simplify()
            except TypeError:
                pass

            t2_pen = T2CharStringPen(v.width, glyphSet=glyph_set)
            qu2cu_pen = Qu2CuPen(t2_pen, max_err=tolerance, all_cubic=all_cubic, reverse_direction=False)
            pathops_path.draw(qu2cu_pen)

            charstring = t2_pen.getCharString()
            charstrings[k] = charstring

        return charstrings

    def get_t2_charstrings(self) -> dict:
        """
        Get CFF charstrings using T2CharStringPen

        :return: CFF charstrings.
        """
        charstrings = {}
        glyph_set = self.font.getGlyphSet()

        for k, v in glyph_set.items():
            # Draw the glyph with T2CharStringPen and get the charstring
            t2_pen = T2CharStringPen(v.width, glyphSet=glyph_set)
            glyph_set[k].draw(t2_pen)
            charstring = t2_pen.getCharString()
            charstrings[k] = charstring

        return charstrings
