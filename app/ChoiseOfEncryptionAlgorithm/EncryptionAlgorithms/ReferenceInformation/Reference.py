from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QMetaObject
from CipherOrDecipher.app.Base.BaseGUI import BaseGUI


class Reference(QMainWindow, BaseGUI):
    def __init__(self, getting_data_from_json, set_text_for_reference):
        super().__init__()
        self.getting_data_from_config = getting_data_from_json
        self._settings_window(self)
        self._forming_form_for_enter_text(
            self,
            **self.getting_data_from_config["parameters_textEdit_for_enter_text"]
        ).setText(set_text_for_reference)
        QMetaObject.connectSlotsByName(self)
