import sys

from PyQt5.QtCore import QMetaObject, QRect, Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QPushButton, QDesktopWidget, QComboBox, QTextEdit, QLabel, \
    QLineEdit
from CipherOrDecipher.app.common import get_data_from_json

GETTING_INFO_ABOUT_REFERENCE = get_data_from_json("referenceInformation.json")


class BaseGUI(object):

    def setupUi(self, base_gui):
        self._settings_window(base_gui)
        self._main_menu(base_gui) if base_gui.choise_of_encryption_algorithm else self._next_step(base_gui)
        self._forming_button(
            base_gui,
            **base_gui.getting_data_from_config["parameters_button_for_quit"]
        ).clicked.connect(self._forming_quit)
        QMetaObject.connectSlotsByName(base_gui)

    def _settings_window(self, base_gui):
        base_gui.resize(
            base_gui.getting_data_from_config["parameters_for_window"]["coord_x"],
            base_gui.getting_data_from_config["parameters_for_window"]["coord_y"]
        )
        self._center(base_gui)
        base_gui.setWindowTitle(base_gui.getting_data_from_config["title"])

    def _center(self, base_gui):
        self.geometry_main_window = QWidget.frameGeometry(base_gui)
        self.center_point_desktop = QDesktopWidget().availableGeometry().center()
        self.geometry_main_window.moveCenter(self.center_point_desktop)
        base_gui.move(self.geometry_main_window.topLeft())

    def _main_menu(self, base_gui):
        self._forming_label(
            base_gui,
            **base_gui.getting_data_from_config["parameters_label_for_choise_encryption_algorithm"]
        )
        self.encryption_algorithms = QComboBox(base_gui)
        self.encryption_algorithms.setGeometry(QRect(
            base_gui.getting_data_from_config["parameters_combobox_for_choise_encryption_algorithm"]["coord_x"],
            base_gui.getting_data_from_config["parameters_combobox_for_choise_encryption_algorithm"]["coord_y"],
            base_gui.getting_data_from_config["parameters_combobox_for_choise_encryption_algorithm"]["weight"],
            base_gui.getting_data_from_config["parameters_combobox_for_choise_encryption_algorithm"]["height"],
        ))

    def _next_step(self, base_gui):
        self.reference = self._forming_button(
            base_gui,
            **base_gui.getting_data_from_config["parameters_button_for_reference"]
        )
        if base_gui.key_is_needed:
            self._forming_lineedit_for_enter_key_cipher_or_decipher(
                base_gui,
                **base_gui.getting_data_from_config["parameters_lineedit_for_enter_key_cipher"]
            )
        self._forming_label(
            base_gui,
            **base_gui.getting_data_from_config["parameters_label_for_enter_text"]
        ).setAlignment(Qt.AlignCenter)
        self.enter_text = self._forming_form_for_enter_text(
            base_gui,
            **base_gui.getting_data_from_config["parameters_textEdit_for_enter_text"]
        )
        self.process_cipher = self._forming_button(
            base_gui,
            **base_gui.getting_data_from_config["parameters_button_for_cipher"]
        )
        self.process_decipher = self._forming_button(
            base_gui,
            **base_gui.getting_data_from_config["parameters_button_for_decipher"]
        )
        self.comeback = self._forming_button(
            self,
            **base_gui.getting_data_from_config["parameters_button_for_comeback"]
        )

    def _forming_label(self, base_gui, title="", coord_x=int(0), coord_y=int(0), weight=int(0), height=int(0)):
        self.forming_info_about_operation = QLabel(title, base_gui)
        self.forming_info_about_operation.setGeometry(QRect(coord_x, coord_y, weight, height))
        return self.forming_info_about_operation

    def _forming_button(self, base_gui, title="", coord_x=int(0), coord_y=int(0)) -> QPushButton:
        self.forming_button = QPushButton(title, base_gui)
        self.forming_button.resize(self.forming_button.sizeHint())
        self.forming_button.move(coord_x, coord_y)
        return self.forming_button

    def _forming_lineedit_for_enter_key_cipher_or_decipher(
            self,
            base_gui,
            coord_x=int(0),
            coord_y=int(0),
            weight=int(0),
            height=int(0)
    ):
        self._forming_label(
            base_gui,
            title='Введите ключ шифрования',
            coord_x=coord_x,
            coord_y=coord_y - 25,
            weight=weight,
            height=height,
        ).setAlignment(Qt.AlignCenter)
        self.encryption_key = QLineEdit(base_gui)
        self.encryption_key.setGeometry(QRect(coord_x, coord_y, weight, height))
        return self.encryption_key

    def _forming_form_for_enter_text(self, base_gui, coord_x=int(0), coord_y=int(0), weight=int(0), height=int(0)):
        self.enter_text = QTextEdit(base_gui)
        self.enter_text.setGeometry(QRect(coord_x, coord_y, weight, height))
        self.enter_text.setAlignment(Qt.AlignTop)
        return self.enter_text

    def _forming_quit(self):
        sys.exit(0)


class BaseEncryptionAlgorithms(QMainWindow, BaseGUI):
    def __init__(self, getting_data_from_config, choise_of_encryption_algorithm, key_is_needed):
        super().__init__()
        self.choise_of_encryption_algorithm = choise_of_encryption_algorithm
        self.key_is_needed = key_is_needed
        self.getting_data_from_config = getting_data_from_config
        self.setupUi(self)

    def _forming_reference(self):
        from CipherOrDecipher.app.ChoiseOfEncryptionAlgorithm.EncryptionAlgorithms.ReferenceInformation.Reference \
            import Reference
        self.window_reference = Reference(
            self.getting_data_from_config_for_reference["reference"],
            GETTING_INFO_ABOUT_REFERENCE.get(self.key_for_getting_reference)
        )
        self.window_reference.show()

    def _comeback(self):
        from CipherOrDecipher.app.app import App
        self.enter_text.clear()
        if self.key_is_needed:
            self.encryption_key.clear()
        self.main_window = App()
        self.main_window.show()
        self.close()
