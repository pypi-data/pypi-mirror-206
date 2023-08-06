import os
import sys
from pathlib import Path

from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import QThreadPool
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QDialog,
    QStyledItemDelegate,
    QListView,
    QDialogButtonBox, QFrame,
)
from fontTools.ttLib import TTCollection

from DRConverter.Lib.converters.options import (
    WebToSFNTOptions,
    TrueTypeToCFFOptions,
    SFNTToWebOptions,
    CFFToTrueTypeOptions,
    Var2StaticOptions,
    TTCollectionToSFNTOptions,
)
from DRConverter.Lib.converters.otf_to_ttf import JobRunner_otf2ttf
from DRConverter.Lib.converters.sfnt_to_web import JobRunner_ft2wf
from DRConverter.Lib.converters.ttc_to_sfnt import JobRunner_ttc2sfnt
from DRConverter.Lib.converters.ttf_to_otf import JobRunner_ttf2otf
from DRConverter.Lib.converters.variable_to_static import JobRunner_vf2i
from DRConverter.Lib.converters.web_to_sfnt import JobRunner_wf2ft
from DRConverter.Lib.font.Font import Font
from DRConverter.Lib.gui.MainWindow import Ui_MainWindow
from DRConverter.Lib.gui.dialogs.otf2ttf_options_dialog import Ui_otf2ttfOptions_Dialog
from DRConverter.Lib.gui.dialogs.output_dialog import Ui_Output
from DRConverter.Lib.gui.dialogs.sfnt2web_options_dialog import Ui_sfnt2webOptions_Dialog
from DRConverter.Lib.gui.dialogs.ttc2sfnt_options_dialog import Ui_ttc2sfntOptions_Dialog
from DRConverter.Lib.gui.dialogs.ttf2otf_options_dialog import Ui_ttf2otfOptions_Dialog
from DRConverter.Lib.gui.dialogs.vf2i_options_dialog import Ui_vf2iOptions_Dialog
from DRConverter.Lib.gui.dialogs.web2sfnt_options_dialog import Ui_web2sfntOptions_Dialog


class FontItem(object):
    file = None
    is_checked = None
    is_enabled = None
    extension = None
    is_sfnt = None
    is_webfont = None
    is_static = None
    is_variable = None
    is_cff = None
    is_ttf = None
    profiles = None


class FilesList(QListView):
    checked = QtCore.pyqtSignal(QtCore.QModelIndex)

    def __init__(self, *args, **kwargs):
        super(FilesList, self).__init__(*args, **kwargs)
        self.setItemDelegate(Delegate(self))


class Delegate(QStyledItemDelegate):
    def editorEvent(self, event, model, option, index):
        checked = index.data(QtCore.Qt.ItemDataRole.CheckStateRole)
        ret = QStyledItemDelegate.editorEvent(self, event, model, option, index)
        if checked != index.data(QtCore.Qt.ItemDataRole.CheckStateRole):
            self.parent().checked.emit(index)
        return ret


class TTF2OTFOptionsDialog(QDialog, Ui_ttf2otfOptions_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class OTF2TTFOptionsDialog(QDialog, Ui_otf2ttfOptions_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class SFNT2WEBOptionsDialog(QDialog, Ui_sfnt2webOptions_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class WEB2SFNTOptionsDialog(QDialog, Ui_web2sfntOptions_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class VF2IOptionsDialog(QDialog, Ui_vf2iOptions_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class TTC2SFNTOptionsDialog(QDialog, Ui_ttc2sfntOptions_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class OutputDialog(QDialog, Ui_Output):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Change the text os Reset and Discard buttons
        self.buttonBox.button(QDialogButtonBox.StandardButton.Reset).setText("Clear log")
        self.buttonBox.button(QDialogButtonBox.StandardButton.Discard).setText("Stop")

        # Disable the close button and remove the what's this button
        self.setWindowFlags(
            self.windowFlags()
            ^ QtCore.Qt.WindowType.WindowCloseButtonHint
            ^ QtCore.Qt.WindowType.WindowContextHelpButtonHint
        )


basedir = os.path.dirname(__file__)

try:
    from ctypes import windll  # Only exists on Windows.

    app_id = "ftcli.ftcli.fontconverter.0.1.0"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
except ImportError:
    pass


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fonts = [FontItem]
        self.input_folder = None
        self.output_folder = None
        self.last_folder = os.path.expanduser("~")
        self.center()

        # Set up the list view
        self.listView_Files = FilesList(self.centralwidget)
        self.listView_Files.setObjectName("listView_Files")
        self.gridLayout_Middle.addWidget(self.listView_Files)
        self.listView_Files.setFrameShape(QFrame.Shape.Box)
        self.files_model = QtGui.QStandardItemModel(self)
        self.item = QtGui.QStandardItem()
        self.listView_Files.setModel(self.files_model)
        self.listView_Files.checked.connect(self.item_checked)
        self.listView_Files.checked.connect(self.set_push_button_options_state)
        self.listView_Files.checked.connect(self.set_push_button_start_state)

        # Connect the Browse Source folder button
        self.pushButton_BrowseSourceFolder.clicked.connect(self.browse_source_folder)
        self.pushButton_BrowseSourceFolder.clicked.connect(self.get_font_items)
        self.pushButton_BrowseSourceFolder.clicked.connect(self.filter_font_items)
        self.pushButton_BrowseSourceFolder.clicked.connect(self.update_list_view)
        self.pushButton_BrowseSourceFolder.clicked.connect(self.set_push_button_start_state)
        self.pushButton_BrowseSourceFolder.clicked.connect(self.set_push_button_options_state)
        self.pushButton_BrowseSourceFolder.clicked.connect(self.set_combobox_conversion_profiles_state)

        # Connect the Browse Destination folder button
        self.pushButton_BrowseDestinationFolder.clicked.connect(self.browse_destination_folder)

        # Connect the Conversion Profile combo box
        self.comboBox_ConversionProfile.currentIndexChanged.connect(self.filter_font_items)
        self.comboBox_ConversionProfile.currentIndexChanged.connect(self.update_list_view)
        self.comboBox_ConversionProfile.currentIndexChanged.connect(self.set_push_button_options_state)
        self.comboBox_ConversionProfile.currentIndexChanged.connect(self.set_push_button_start_state)

        # Connect the Conversion Options tool button
        self.pushButton_ConversionOptions.clicked.connect(self.show_options_dialog)

        # Connect the Start button
        self.pushButton_Start.clicked.connect(self.start_process)
        self.pushButton_Start.clicked.connect(self.show_output_dialog)
        self.pushButton_Start.clicked.connect(self.get_font_items)
        self.pushButton_Start.clicked.connect(self.filter_font_items)
        self.pushButton_Start.clicked.connect(self.update_list_view)

        # Initialize the runner
        self.runner = None
        self.threadpool = QThreadPool()

        # Set up output dialog
        self.output_dialog = OutputDialog()
        self.output_dialog.buttonBox.button(QDialogButtonBox.StandardButton.Reset).clicked.connect(self.clear_log)
        self.output_dialog.buttonBox.button(QDialogButtonBox.StandardButton.Discard).clicked.connect(self.stop_runner)

        # Setup converter options
        self.ft2wf_options = SFNTToWebOptions()
        self.wf2ft_options = WebToSFNTOptions()
        self.ttf2otf_options = TrueTypeToCFFOptions()
        self.otf2ttf_options = CFFToTrueTypeOptions()
        self.vf2i_options = Var2StaticOptions()
        self.ttc2sfnt_options = TTCollectionToSFNTOptions()

        # Init wf2ft_dlg
        self.wf2ft_dlg = WEB2SFNTOptionsDialog()
        self.wf2ft_dlg.buttonBox.button(QDialogButtonBox.StandardButton.Save).clicked.connect(self.save_wf2ft_options)
        self.wf2ft_dlg.buttonBox.button(QDialogButtonBox.StandardButton.Save).clicked.connect(self.init_wf2ft_dialog)
        self.wf2ft_dlg.buttonBox.button(QDialogButtonBox.StandardButton.Save).clicked.connect(self.filter_font_items)
        self.wf2ft_dlg.buttonBox.button(QDialogButtonBox.StandardButton.Save).clicked.connect(self.update_list_view)
        self.wf2ft_dlg.buttonBox.button(QDialogButtonBox.StandardButton.RestoreDefaults).clicked.connect(
            self.reset_wf2ft_options)
        self.wf2ft_dlg.buttonBox.button(QDialogButtonBox.StandardButton.RestoreDefaults).clicked.connect(
            self.init_wf2ft_dialog)

        # Init ft2wf_dlg
        self.ft2wf_dlg = SFNT2WEBOptionsDialog()
        self.ft2wf_dlg.buttonBox.button(QDialogButtonBox.StandardButton.Save).clicked.connect(self.save_ft2wf_options)
        self.ft2wf_dlg.buttonBox.button(QDialogButtonBox.StandardButton.Save).clicked.connect(self.init_ft2wf_dialog)
        self.ft2wf_dlg.buttonBox.button(QDialogButtonBox.StandardButton.Save).clicked.connect(self.filter_font_items)
        self.ft2wf_dlg.buttonBox.button(QDialogButtonBox.StandardButton.Save).clicked.connect(self.update_list_view)
        self.ft2wf_dlg.buttonBox.button(QDialogButtonBox.StandardButton.RestoreDefaults).clicked.connect(
            self.reset_ft2wf_options)
        self.ft2wf_dlg.buttonBox.button(QDialogButtonBox.StandardButton.RestoreDefaults).clicked.connect(
            self.init_ft2wf_dialog)

        # Init tt2f2otf_dlg
        self.ttf2otf_dlg = TTF2OTFOptionsDialog()
        self.ttf2otf_dlg.buttonBox.button(QDialogButtonBox.StandardButton.Save).clicked.connect(
            self.save_ttf2otf_options)
        self.ttf2otf_dlg.buttonBox.button(QDialogButtonBox.StandardButton.Save).clicked.connect(
            self.init_ttf2otf_dialog)
        self.ttf2otf_dlg.buttonBox.button(QDialogButtonBox.StandardButton.RestoreDefaults).clicked.connect(
            self.reset_ttf2otf_options)
        self.ttf2otf_dlg.buttonBox.button(QDialogButtonBox.StandardButton.RestoreDefaults).clicked.connect(
            self.init_ttf2otf_dialog)

        # Init otf2ttf_dlg
        self.otf2ttf_dlg = OTF2TTFOptionsDialog()
        self.otf2ttf_dlg.buttonBox.button(QDialogButtonBox.StandardButton.Save).clicked.connect(
            self.save_otf2ttf_options)
        self.otf2ttf_dlg.buttonBox.button(QDialogButtonBox.StandardButton.Save).clicked.connect(
            self.init_otf2ttf_dialog)
        self.otf2ttf_dlg.buttonBox.button(QDialogButtonBox.StandardButton.RestoreDefaults).clicked.connect(
            self.reset_otf2ttf_options)
        self.otf2ttf_dlg.buttonBox.button(QDialogButtonBox.StandardButton.RestoreDefaults).clicked.connect(
            self.init_otf2ttf_dialog)

        # Init vf2i_dlg
        self.vf2i_dlg = VF2IOptionsDialog()
        self.vf2i_dlg.buttonBox.button(QDialogButtonBox.StandardButton.Save).clicked.connect(self.save_vf2i_options)
        self.vf2i_dlg.buttonBox.button(QDialogButtonBox.StandardButton.RestoreDefaults).clicked.connect(
            self.reset_vf2i_options)
        self.vf2i_dlg.buttonBox.button(QDialogButtonBox.StandardButton.RestoreDefaults).clicked.connect(
            self.init_vf2i_dialog)

        # Init ttc2sfnt_dlg
        self.ttc2sfnt_dlg = TTC2SFNTOptionsDialog()
        self.ttc2sfnt_dlg.buttonBox.button(QDialogButtonBox.StandardButton.Save).clicked.connect(
            self.save_ttc2sfnt_options)
        self.ttc2sfnt_dlg.buttonBox.button(QDialogButtonBox.StandardButton.RestoreDefaults).clicked.connect(
            self.reset_ttc2sfnt_options
        )
        self.ttc2sfnt_dlg.buttonBox.button(QDialogButtonBox.StandardButton.RestoreDefaults).clicked.connect(
            self.init_ttc2sfnt_dialog)

        # Show the app
        self.show()

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def item_checked(self, index):
        item = self.files_model.itemFromIndex(index)
        if item.checkState() == QtCore.Qt.CheckState.Checked:
            self.fonts[item.index().row()].is_checked = True
        else:
            self.fonts[item.index().row()].is_checked = False

    def browse_source_folder(self):
        dlg = QFileDialog(self)
        dlg.setWindowTitle("Browse source folder")
        dlg.setFileMode(QFileDialog.FileMode.Directory)
        dlg.setViewMode(QFileDialog.ViewMode.List)
        dlg.setDirectory(self.last_folder)

        if dlg.exec():
            self.input_folder = str(Path(dlg.selectedFiles()[0]))
            if self.input_folder:
                self.lineEdit_SourceFolder.setText(self.input_folder)
                self.last_folder = self.input_folder
                self.output_folder = self.input_folder
                self.lineEdit_DestinationFolder.setText(self.input_folder)

    def browse_destination_folder(self):
        dlg = QFileDialog(self)
        dlg.setWindowTitle("Browse destination folder")
        dlg.setFileMode(QFileDialog.FileMode.Directory)
        dlg.setViewMode(QFileDialog.ViewMode.List)
        dlg.setDirectory(self.last_folder)

        if dlg.exec():
            self.output_folder = str(Path(dlg.selectedFiles()[0]))
            if self.output_folder:
                self.lineEdit_DestinationFolder.setText(self.output_folder)

    def get_font_items(self):
        self.fonts = []
        if self.input_folder:
            files = [str(Path(os.path.join(self.input_folder, file))) for file in os.listdir(self.input_folder)]
            for file in files:
                try:
                    font = Font(file)
                    data = FontItem()
                    data.file = file
                    data.extension = font.get_real_extension()
                    data.is_variable = True if font.is_variable else False
                    data.is_checked = True
                    data.is_enabled = True
                    data.profiles = [1, 2, 3, 4, 5]
                    if font.flavor is None:  # SFNT font
                        data.profiles.remove(1)
                    else:  # Web font
                        data.profiles.remove(2)
                    if not self.wf2ft_options.woff2 and font.flavor == "woff2":
                        data.profiles.remove(1)
                    if not self.wf2ft_options.woff and font.flavor == "woff":
                        data.profiles.remove(1)
                    if font.is_true_type or font.is_variable:  # TTF or variable font
                        data.profiles.remove(3)
                    if font.is_cff or font.is_variable:  # CFF or variable font
                        data.profiles.remove(4)
                    if not font.is_variable:  # Static font
                        data.profiles.remove(5)

                    data.is_webfont = True if font.get_real_extension() in (".woff", ".woff2") else False
                    data.is_sfnt = False if font.get_real_extension() in (".woff", ".woff2") else True
                    data.is_cff = True if font.is_cff else False
                    data.is_ttf = True if font.is_true_type else False

                    self.fonts.append(data)

                except:
                    try:
                        TTCollection(file)
                        data = FontItem()
                        data.file = file
                        data.profiles = [6]
                        data.is_checked = True
                        data.is_enabled = True

                        self.fonts.append(data)

                    except:
                        pass

    def filter_font_items(self):
        for font in self.fonts:
            if self.comboBox_ConversionProfile.currentIndex() == 0:  # No profile selected
                font.is_enabled = False
                font.is_checked = False
            elif self.comboBox_ConversionProfile.currentIndex() in font.profiles:
                font.is_enabled = True
                font.is_checked = True
            else:
                font.is_enabled = False
                font.is_checked = False

    def update_list_view(self):
        self.files_model.clear()
        for font in self.fonts:
            item = QtGui.QStandardItem(str(os.path.basename(font.file)))
            item.setEditable(False)
            item.setCheckable(True)
            if self.comboBox_ConversionProfile.currentIndex() == 0:
                item.setCheckable(False)
                item.setEnabled(False)
            elif self.comboBox_ConversionProfile.currentIndex() in font.profiles:
                item.setCheckable(True)
                item.setEnabled(True)
                item.setCheckState(QtCore.Qt.CheckState.Checked)
            else:
                item.setCheckable(False)
                item.setEnabled(False)

            self.files_model.appendRow(item)

    def set_combobox_conversion_profiles_state(self):
        if len(self.fonts) > 0:
            self.comboBox_ConversionProfile.setEnabled(True)
        else:
            self.comboBox_ConversionProfile.setDisabled(True)
            self.comboBox_ConversionProfile.setCurrentIndex(0)

    def set_push_button_start_state(self):
        selected_fonts = [ft for ft in self.fonts if ft.is_checked]
        if len(selected_fonts) > 0 and self.comboBox_ConversionProfile.currentIndex() != 0:
            self.pushButton_Start.setEnabled(True)
        else:
            self.pushButton_Start.setDisabled(True)

    def set_push_button_options_state(self):
        if self.comboBox_ConversionProfile.currentIndex() == 0:
            self.pushButton_ConversionOptions.setDisabled(True)
        else:
            self.pushButton_ConversionOptions.setEnabled(True)

    def show_options_dialog(self):
        if self.comboBox_ConversionProfile.currentIndex() == 1:
            self.init_wf2ft_dialog()
            self.wf2ft_dlg.exec()

        elif self.comboBox_ConversionProfile.currentIndex() == 2:
            self.init_ft2wf_dialog()
            self.ft2wf_dlg.exec()

        elif self.comboBox_ConversionProfile.currentIndex() == 3:
            self.init_otf2ttf_dialog()
            self.otf2ttf_dlg.exec()

        elif self.comboBox_ConversionProfile.currentIndex() == 4:
            self.init_ttf2otf_dialog()
            self.ttf2otf_dlg.exec()

        elif self.comboBox_ConversionProfile.currentIndex() == 5:
            self.init_vf2i_dialog()
            self.vf2i_dlg.exec()

        elif self.comboBox_ConversionProfile.currentIndex() == 6:
            self.init_ttc2sfnt_dialog()
            self.ttc2sfnt_dlg.exec()

    def init_wf2ft_dialog(self):
        if self.wf2ft_options.woff and self.wf2ft_options.woff2:
            self.wf2ft_dlg.inputFormat_comboBox.setCurrentIndex(0)

        if self.wf2ft_options.woff and not self.wf2ft_options.woff2:
            self.wf2ft_dlg.inputFormat_comboBox.setCurrentIndex(1)

        if self.wf2ft_options.woff2 and not self.wf2ft_options.woff:
            self.wf2ft_dlg.inputFormat_comboBox.setCurrentIndex(2)

        if self.wf2ft_options.overwrite:
            self.wf2ft_dlg.overwrite_checkBox.setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.wf2ft_dlg.overwrite_checkBox.setCheckState(QtCore.Qt.CheckState.Unchecked)

        if self.wf2ft_options.recalc_timestamp:
            self.wf2ft_dlg.recalcTimestamp_checkBox.setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.wf2ft_dlg.recalcTimestamp_checkBox.setCheckState(QtCore.Qt.CheckState.Unchecked)

    def save_wf2ft_options(self):
        if self.wf2ft_dlg.inputFormat_comboBox.currentIndex() == 0:
            self.wf2ft_options.woff = True
            self.wf2ft_options.woff2 = True

        if self.wf2ft_dlg.inputFormat_comboBox.currentIndex() == 1:
            self.wf2ft_options.woff = True
            self.wf2ft_options.woff2 = False

        if self.wf2ft_dlg.inputFormat_comboBox.currentIndex() == 2:
            self.wf2ft_options.woff = False
            self.wf2ft_options.woff2 = True

        for font in self.fonts:
            if font.extension == ".woff":
                if not self.wf2ft_options.woff:
                    if 1 in font.profiles:
                        font.profiles.remove(1)
                else:
                    font.profiles.append(1)

            if font.extension == ".woff2":
                if not self.wf2ft_options.woff2:
                    if 1 in font.profiles:
                        font.profiles.remove(1)
                else:
                    font.profiles.append(1)

            font.profiles = list(set(font.profiles))

        self.wf2ft_options.overwrite = True if self.wf2ft_dlg.overwrite_checkBox.isChecked() else False

        self.wf2ft_options.recalc_timestamp = True if self.wf2ft_dlg.recalcTimestamp_checkBox.isChecked() else False

    def reset_wf2ft_options(self):
        self.wf2ft_options = WebToSFNTOptions()

    def init_ft2wf_dialog(self):
        if self.ft2wf_options.woff and not self.ft2wf_options.woff2:
            self.ft2wf_dlg.outputFormat_comboBox.setCurrentIndex(1)

        elif self.ft2wf_options.woff2 and not self.ft2wf_options.woff:
            self.ft2wf_dlg.outputFormat_comboBox.setCurrentIndex(2)

        else:
            self.ft2wf_dlg.outputFormat_comboBox.setCurrentIndex(0)

        if self.ft2wf_options.overwrite:
            self.ft2wf_dlg.overwrite_checkBox.setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.ft2wf_dlg.overwrite_checkBox.setCheckState(QtCore.Qt.CheckState.Unchecked)

        if self.ft2wf_options.recalc_timestamp:
            self.ft2wf_dlg.recalcTimestamp_checkBox.setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.ft2wf_dlg.recalcTimestamp_checkBox.setCheckState(QtCore.Qt.CheckState.Unchecked)

    def save_ft2wf_options(self):
        if self.ft2wf_dlg.outputFormat_comboBox.currentIndex() == 0:
            self.ft2wf_options.woff = True
            self.ft2wf_options.woff2 = True

        if self.ft2wf_dlg.outputFormat_comboBox.currentIndex() == 1:
            self.ft2wf_options.woff = True
            self.ft2wf_options.woff2 = False

        if self.ft2wf_dlg.outputFormat_comboBox.currentIndex() == 2:
            self.ft2wf_options.woff = False
            self.ft2wf_options.woff2 = True

        self.ft2wf_options.overwrite = True if self.ft2wf_dlg.overwrite_checkBox.isChecked() else False

        self.ft2wf_options.recalc_timestamp = True if self.ft2wf_dlg.recalcTimestamp_checkBox.isChecked() else False

    def reset_ft2wf_options(self):
        self.ft2wf_options = SFNTToWebOptions()

    def init_otf2ttf_dialog(self):
        self.otf2ttf_dlg.tolerance_doubleSpinBox.setValue(self.otf2ttf_options.max_err)

        if self.otf2ttf_options.recalc_timestamp:
            self.otf2ttf_dlg.recalcTimestamp_checkBox.setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.otf2ttf_dlg.recalcTimestamp_checkBox.setCheckState(QtCore.Qt.CheckState.Unchecked)

        if self.otf2ttf_options.overwrite:
            self.otf2ttf_dlg.overwrite_checkBox.setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.otf2ttf_dlg.overwrite_checkBox.setCheckState(QtCore.Qt.CheckState.Unchecked)

    def save_otf2ttf_options(self):
        self.otf2ttf_options.max_err = self.otf2ttf_dlg.tolerance_doubleSpinBox.value()

        if self.otf2ttf_dlg.recalcTimestamp_checkBox.isChecked():
            self.otf2ttf_options.recalc_timestamp = True
        else:
            self.otf2ttf_options.recalc_timestamp = False

        if self.otf2ttf_dlg.overwrite_checkBox.isChecked():
            self.otf2ttf_options.overwrite = True
        else:
            self.otf2ttf_options.overwrite = False

    def reset_otf2ttf_options(self):
        self.otf2ttf_options = CFFToTrueTypeOptions()

    def init_ttf2otf_dialog(self):
        self.ttf2otf_dlg.tolerance_doubleSpinBox.setValue(self.ttf2otf_options.tolerance)

        if self.ttf2otf_options.remove_glyphs:
            self.ttf2otf_dlg.removeGlyphs_checkBox.setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.ttf2otf_dlg.removeGlyphs_checkBox.setCheckState(QtCore.Qt.CheckState.Unchecked)

        if self.ttf2otf_options.subroutinize:
            self.ttf2otf_dlg.subroutinize_checkBox.setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.ttf2otf_dlg.subroutinize_checkBox.setCheckState(QtCore.Qt.CheckState.Unchecked)

        if self.ttf2otf_options.check_outlines:
            self.ttf2otf_dlg.checkOutlines_checkBox.setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.ttf2otf_dlg.checkOutlines_checkBox.setCheckState(QtCore.Qt.CheckState.Unchecked)

        if self.ttf2otf_options.safe_mode:
            self.ttf2otf_dlg.safeMode_checkBox.setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.ttf2otf_dlg.safeMode_checkBox.setCheckState(QtCore.Qt.CheckState.Unchecked)

        if self.ttf2otf_options.scale_upm:
            self.ttf2otf_dlg.scaleUPM_checkBox.setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.ttf2otf_dlg.scaleUPM_checkBox.setCheckState(QtCore.Qt.CheckState.Unchecked)

        if self.ttf2otf_options.recalc_timestamp:
            self.ttf2otf_dlg.recalcTimestamp_checkBox.setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.ttf2otf_dlg.recalcTimestamp_checkBox.setCheckState(QtCore.Qt.CheckState.Unchecked)

        if self.ttf2otf_options.overwrite:
            self.ttf2otf_dlg.overwrite_checkBox.setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.ttf2otf_dlg.overwrite_checkBox.setCheckState(QtCore.Qt.CheckState.Unchecked)

    def save_ttf2otf_options(self):
        self.ttf2otf_options.tolerance = self.ttf2otf_dlg.tolerance_doubleSpinBox.value()

        if self.ttf2otf_dlg.removeGlyphs_checkBox.isChecked():
            self.ttf2otf_options.remove_glyphs = True
        else:
            self.ttf2otf_options.remove_glyphs = False

        if self.ttf2otf_dlg.subroutinize_checkBox.isChecked():
            self.ttf2otf_options.subroutinize = True
        else:
            self.ttf2otf_options.subroutinize = False

        if self.ttf2otf_dlg.checkOutlines_checkBox.isChecked():
            self.ttf2otf_options.check_outlines = True
        else:
            self.ttf2otf_options.check_outlines = False

        if self.ttf2otf_dlg.safeMode_checkBox.isChecked():
            self.ttf2otf_options.safe_mode = True
        else:
            self.ttf2otf_options.safe_mode = False

        if self.ttf2otf_dlg.scaleUPM_checkBox.isChecked():
            self.ttf2otf_options.scale_upm = True
        else:
            self.ttf2otf_options.scale_upm = False

        if self.ttf2otf_dlg.recalcTimestamp_checkBox.isChecked():
            self.ttf2otf_options.recalc_timestamp = True
        else:
            self.ttf2otf_options.recalc_timestamp = False

        if self.ttf2otf_dlg.overwrite_checkBox.isChecked():
            self.ttf2otf_options.overwrite = True
        else:
            self.ttf2otf_options.overwrite = False

    def reset_ttf2otf_options(self):
        self.ttf2otf_options = TrueTypeToCFFOptions()

    def init_vf2i_dialog(self):
        if self.vf2i_options.update_name_table:
            self.vf2i_dlg.updateNameTable_checkBox.setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.vf2i_dlg.updateNameTable_checkBox.setCheckState(QtCore.Qt.CheckState.Unchecked)

        if self.vf2i_options.cleanup:
            self.vf2i_dlg.cleanupInstances_checkBox.setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.vf2i_dlg.cleanupInstances_checkBox.setCheckState(QtCore.Qt.CheckState.Unchecked)

        if self.vf2i_options.recalc_timestamp:
            self.vf2i_dlg.recalcTimestamp_checkBox.setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.vf2i_dlg.recalcTimestamp_checkBox.setCheckState(QtCore.Qt.CheckState.Unchecked)

        if self.vf2i_options.overwrite:
            self.vf2i_dlg.overwrite_checkBox.setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.vf2i_dlg.overwrite_checkBox.setCheckState(QtCore.Qt.CheckState.Unchecked)

    def save_vf2i_options(self):
        self.vf2i_options.cleanup = True if self.vf2i_dlg.cleanupInstances_checkBox.isChecked() else False

        self.vf2i_options.update_name_table = True if self.vf2i_dlg.updateNameTable_checkBox.isChecked() else False

        self.vf2i_options.recalc_timestamp = True if self.vf2i_dlg.recalcTimestamp_checkBox.isChecked() else False

        self.vf2i_options.overwrite = True if self.vf2i_dlg.overwrite_checkBox.isChecked() else False

    def reset_vf2i_options(self):
        self.vf2i_options = Var2StaticOptions()

    def init_ttc2sfnt_dialog(self):
        if self.ttc2sfnt_options.overwrite:
            self.ttc2sfnt_dlg.overwrite_checkBox.setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.ttc2sfnt_dlg.overwrite_checkBox.setCheckState(QtCore.Qt.CheckState.Unchecked)

        if self.ttc2sfnt_options.recalc_timestamp:
            self.ttc2sfnt_dlg.recalcTimestamp_checkBox.setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.ttc2sfnt_dlg.recalcTimestamp_checkBox.setCheckState(QtCore.Qt.CheckState.Unchecked)

    def save_ttc2sfnt_options(self):
        self.ttc2sfnt_options.overwrite = True if self.ttc2sfnt_dlg.overwrite_checkBox.isChecked() else False
        self.ttc2sfnt_options.recalc_timestamp = (
            True if self.ttc2sfnt_dlg.recalcTimestamp_checkBox.isChecked() else False
        )

    def reset_ttc2sfnt_options(self):
        self.ttc2sfnt_options = TTCollectionToSFNTOptions()

    def start_process(self):
        self.output_dialog.buttonBox.button(QDialogButtonBox.StandardButton.Reset).setDisabled(True)
        self.output_dialog.buttonBox.button(QDialogButtonBox.StandardButton.Discard).setEnabled(True)
        self.output_dialog.buttonBox.button(QDialogButtonBox.StandardButton.Close).setDisabled(True)

        files = [font.file for font in self.fonts if font.is_checked]

        # Web to SFNT
        if self.comboBox_ConversionProfile.currentIndex() == 1:
            self.runner = JobRunner_wf2ft(files)
            self.runner.options = self.wf2ft_options

        # SFNT to Web
        elif self.comboBox_ConversionProfile.currentIndex() == 2:
            self.runner = JobRunner_ft2wf(files)
            self.runner.options = self.ft2wf_options

        # CFF to TrueType
        elif self.comboBox_ConversionProfile.currentIndex() == 3:
            self.runner = JobRunner_otf2ttf(files)
            self.runner.options = self.otf2ttf_options

        # TrueType to CFF
        elif self.comboBox_ConversionProfile.currentIndex() == 4:
            self.runner = JobRunner_ttf2otf(files)
            self.runner.options = self.ttf2otf_options

        # Variable to static
        elif self.comboBox_ConversionProfile.currentIndex() == 5:
            self.runner = JobRunner_vf2i(files)
            self.runner.options = self.vf2i_options

        elif self.comboBox_ConversionProfile.currentIndex() == 6:
            self.runner = JobRunner_ttc2sfnt(files)
            self.runner.options = self.ttc2sfnt_options

        else:
            pass

        self.runner.options.output_dir = self.output_folder
        self.runner.signals.progress.connect(self.print_process_output)
        self.runner.signals.finished.connect(self.runner_finished)
        self.threadpool.thread().started.connect(self.runner_started)
        self.threadpool.start(self.runner)

    def runner_started(self):
        self.output_dialog.buttonBox.button().setDisabled(True)
        self.output_dialog.buttonBox.button(QDialogButtonBox.StandardButton.Discard).setEnabled(True)
        self.output_dialog.buttonBox.button(QDialogButtonBox.StandardButton.Close).setDisabled(True)

    def stop_runner(self):
        if self.runner:
            self.runner.is_killed = True

    def runner_finished(self):
        if self.runner.is_killed:
            self.output_dialog.plainTextEdit.appendPlainText("\nPROCESS ABORTED")
        else:
            self.output_dialog.plainTextEdit.appendPlainText("\nPROCESS COMPLETED")
        self.output_dialog.buttonBox.button(QDialogButtonBox.StandardButton.Reset).setEnabled(True)
        self.output_dialog.buttonBox.button(QDialogButtonBox.StandardButton.Discard).setDisabled(True)
        self.output_dialog.buttonBox.button(QDialogButtonBox.StandardButton.Close).setEnabled(True)
        self.runner = None

    def show_output_dialog(self):
        self.output_dialog.exec()

    def clear_log(self):
        self.output_dialog.plainTextEdit.clear()

    def print_process_output(self, s):
        self.output_dialog.plainTextEdit.appendPlainText(s)

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(os.path.join(basedir, "icons", "icon.ico")))
    w = MainWindow()
    w.setWindowTitle("DR Converter")
    w.show()
    app.exec()


if __name__ == "__main__":
    main()
