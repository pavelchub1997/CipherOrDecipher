import sys

from PyQt5.QtCore import QMetaObject, QRect, Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QPushButton, QDesktopWidget, QComboBox, QTextEdit, QLabel, \
    QLineEdit

from CipherOrDecipher.app.base.base import BaseGraphicalUserInterface
from CipherOrDecipher.app.common import get_data_from_json

GETTING_INFO_ABOUT_REFERENCE = get_data_from_json("referenceInformation.json")


class GraphicalUserInterface(BaseGraphicalUserInterface):

    def setup_user_interface(self, base_gui):
        WindowDisplaySettings(base_gui)
        QMetaObject.connectSlotsByName(base_gui)


class WindowDisplaySettings:
    def __init__(self, obj_cls):
        self.__title = obj_cls.getting_data_from_config["title"]
        self.__coord_x = obj_cls.getting_data_from_config["parameters_for_custom_window"]["coord_x"]
        self.__coord_y = obj_cls.getting_data_from_config["parameters_for_custom_window"]["coord_y"]
        self.__create_custom_window(obj_cls)

    def __create_custom_window(self, base_gui):
        base_gui.resize(self.__coord_x, self.__coord_y)
        self.__center(base_gui)
        base_gui.setWindowTitle(self.__title)

    def __center(self, base_gui):
        self.geometry_main_window = QWidget.frameGeometry(base_gui)
        self.center_point_desktop = QDesktopWidget().availableGeometry().center()
        self.geometry_main_window.moveCenter(self.center_point_desktop)
        base_gui.move(self.geometry_main_window.topLeft())


class MainMenu(GraphicalUserInterface):
    def __init__(self, obj_cls):
        super().__init__()
        self.setup_user_interface(obj_cls)
        Title(obj_cls, obj_cls.getting_data_from_config["parameters_for_icon_position"])
        EncryptionAlgorithms(obj_cls)
        obj_cls.continue_button = Button(
            **obj_cls.getting_data_from_config["parameters_button_for_continue_work"]
        ).set_button_position(obj_cls)
        Quit(obj_cls)


class EncryptionAlgorithms:
    def __init__(self, obj_cls):
        self.list_dropdown_position: dict = obj_cls.getting_data_from_config["list_dropdown_position"]
        obj_cls.encryption_algorithms = QComboBox(obj_cls)
        Dimension(obj_cls.encryption_algorithms, **self.list_dropdown_position)


class CipherOrDecipherData(GraphicalUserInterface):
    def __init__(self, obj_cls):
        super().__init__()
        self.setup_user_interface(obj_cls)
        obj_cls.help_button = Button(
            **obj_cls.getting_data_from_config["parameters_button_for_reference"]
        ).set_button_position(obj_cls)
        EnterData(obj_cls)
        obj_cls.cipher_button = Button(
            **obj_cls.getting_data_from_config["parameters_button_for_cipher"]
        ).set_button_position(obj_cls)
        obj_cls.decipher_button = Button(
            **obj_cls.getting_data_from_config["parameters_button_for_decipher"]
        ).set_button_position(obj_cls)
        obj_cls.comeback = Button(
            **obj_cls.getting_data_from_config["parameters_button_for_comeback"]
        ).set_button_position(obj_cls)
        Quit(obj_cls)


class EnterData:
    def __init__(self, obj_cls):
        self.parameters_lineedit_for_enter_key_cipher = \
            obj_cls.getting_data_from_config.get("parameters_lineedit_for_enter_key_cipher")
        if self.parameters_lineedit_for_enter_key_cipher is not None:
            self.__create_form_for_enter_key(obj_cls)
        self.__create_form_for_enter_text(obj_cls)

    @staticmethod
    def __create_form_for_enter_text(obj_cls):
        Title(obj_cls, obj_cls.getting_data_from_config["parameters_label_for_enter_text"]).set_title_by_center()
        obj_cls.enter_text = QTextEdit(obj_cls)
        Dimension(obj_cls.enter_text, **obj_cls.getting_data_from_config["parameters_textEdit_for_enter_text"])
        obj_cls.enter_text.setAlignment(Qt.AlignTop)

    def __create_form_for_enter_key(self, obj_cls):
        Title(obj_cls, obj_cls.getting_data_from_config["parameters_label_for_enter_key_cipher"]).set_title_by_center()
        obj_cls.encryption_key = QLineEdit(obj_cls)
        Dimension(obj_cls.encryption_key, **self.parameters_lineedit_for_enter_key_cipher)


class Quit:
    def __init__(self, obj_cls):
        obj_cls.quit = Button(
            **obj_cls.getting_data_from_config["parameters_button_for_quit"]
        ).set_button_position(obj_cls).clicked.connect(self.__create_quit)

    @staticmethod
    def __create_quit():
        sys.exit(0)


class Title:
    def __init__(self, obj_cls, parameters_for_creating_title: dict):
        self.__title_creating = QLabel(parameters_for_creating_title['title'], obj_cls)
        Dimension(self.__title_creating, **parameters_for_creating_title)

    def set_title_by_center(self):
        self.__title_creating.setAlignment(Qt.AlignCenter)


class Button:
    def __init__(self, **parameters_for_creating_button: dict):
        self.__title = parameters_for_creating_button["title"]
        self.__coord_x = parameters_for_creating_button["coord_x"]
        self.__coord_y = parameters_for_creating_button["coord_y"]

    def set_button_position(self, obj_cls):
        obj_cls.button_creating = QPushButton(self.__title, obj_cls)
        obj_cls.button_creating.resize(obj_cls.button_creating.sizeHint())
        obj_cls.button_creating.move(self.__coord_x, self.__coord_y)
        return obj_cls.button_creating


class Dimension:
    def __init__(self, parameter: QWidget, **parameters_for_size: dict):
        self.__coord_x = parameters_for_size["coord_x"]
        self.__coord_y = parameters_for_size["coord_y"]
        self.__weight = parameters_for_size["weight"]
        self.__height = parameters_for_size["height"]
        parameter.setGeometry(QRect(self.__coord_x, self.__coord_y, self.__weight, self.__height))


class BaseEncryptionAlgorithms(QMainWindow):
    def __init__(self, getting_data_from_config):
        super().__init__()
        self.getting_data_from_config = getting_data_from_config
        CipherOrDecipherData(self)

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
        self.main_window = App()
        self.main_window.show()
        self.close()
