from .Functions import select_combo_box_data, remove_list_duplicates, is_flatpak
from .ui_compiled.SettingsDialog import Ui_SettingsDialog
from PyQt6.QtCore import QCoreApplication, QLocale
from PyQt6.QtWidgets import QDialog, QFileDialog
from .Languages import get_language_names
from typing import TYPE_CHECKING
from .Settings import Settings
import sys
import os


if TYPE_CHECKING:
    from .Environment import Environment
    from .MainWindow import MainWindow


class SettingsDialog(QDialog, Ui_SettingsDialog):
    def __init__(self, env: "Environment", main_window: "MainWindow") -> None:
        super().__init__()

        self.setupUi(self)

        self._env = env
        self._main_window = main_window

        found_translations = False
        language_names = get_language_names()
        self.language_box.addItem(QCoreApplication.translate("SettingsDialog", "System language"), "default")
        self.language_box.addItem("English", "en")
        for i in os.listdir(os.path.join(env.program_dir, "translations")):
            if i.endswith(".qm"):
                lang = i.removeprefix("jdAnimatedImageEditor_").removesuffix(".qm")
                self.language_box.addItem(language_names.get(lang, lang), lang)
                found_translations = True
        if not found_translations:
             print("No compiled translations found. Please run tools/BuildTranslations to build the Translations.py.", file=sys.stderr)

        self.window_title_box.addItem("jdAnimatedImageEditor", "programName")
        self.window_title_box.addItem(QCoreApplication.translate("SettingsDialog", "Filename") + " - jdAnimatedImageEditor", "fileName")
        self.window_title_box.addItem(QCoreApplication.translate("SettingsDialog", "Path") + " - jdAnimatedImageEditor", "filePath")

        if is_flatpak():
            # Flatpak should only use the bundled FFmpeg
            self.ffmpeg_group_box.hide()
            self.resize(self.minimumSize())

        self.ffmpeg_path_checkbox.toggled.connect(self._update_ffmpeg_path_enabled)
        self.ffmpeg_path_button.clicked.connect(self._browse_ffmpeg_path_clicked)
        self.reset_button.clicked.connect(lambda: self._update_widgets(Settings()))
        self.ok_button.clicked.connect(self._ok_button_clicked)
        self.cancel_button.clicked.connect(self.close)

    def _update_ffmpeg_path_enabled(self):
        enabled = self.ffmpeg_path_checkbox.isChecked()
        self.ffmpeg_path_label.setEnabled(enabled)
        self.ffmpeg_path_edit.setEnabled(enabled)
        self.ffmpeg_path_button.setEnabled(enabled)

    def _browse_ffmpeg_path_clicked(self):
        path = QFileDialog.getOpenFileName(self, directory=os.path.dirname(self.ffmpeg_path_edit.text()))[0]
        if path != "":
            self.ffmpeg_path_edit.setText(path)

    def _update_widgets(self, settings: Settings):
        select_combo_box_data(self.language_box, settings.get("language"))
        self.recent_files_spin_box.setValue(settings.get("recentFilesLength"))
        select_combo_box_data(self.window_title_box, settings.get("windowTitleType"))
        self.title_modified_check_box.setChecked(settings.get("windowTitleFileModified"))
        self.ask_save_check_box.setChecked(settings.get("checkSaveBeforeClosing"))
        self.ffmpeg_path_checkbox.setChecked(settings.get("useCustomFFmpegPath"))
        self.ffmpeg_path_edit.setText(settings.get("customFFmpegPath"))

        self._update_ffmpeg_path_enabled()

    def _ok_button_clicked(self):
        self._env.settings.set("language", self.language_box.currentData())
        self._env.settings.set("recentFilesLength", self.recent_files_spin_box.value())
        self._env.settings.set("windowTitleType", self.window_title_box.currentData())
        self._env.settings.set("windowTitleFileModified", self.title_modified_check_box.isChecked())
        self._env.settings.set("checkSaveBeforeClosing", self.ask_save_check_box.isChecked())
        self._env.settings.set("useCustomFFmpegPath", self.ffmpeg_path_checkbox.isChecked())
        self._env.settings.set("customFFmpegPath", self.ffmpeg_path_edit.text())

        self._env.settings.save(os.path.join(self._env.data_dir, "settings.json"))

        self._env.recent_files = remove_list_duplicates(self._env.recent_files)[:self._env.settings.get("recentFilesLength")]
        self._env.save_recent_files()

        self._main_window.update_window_title()

        self.close()

    def open_dialog(self) -> None:
        self._update_widgets(self._env.settings)
        self.exec()
