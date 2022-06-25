from CipherOrDecipher.app.graphical_user_interface.graphical_user_interface import *


class Reference(QMainWindow, GraphicalUserInterface):
    def __init__(self, getting_data_from_json, set_text_for_reference):
        super().__init__()
        self.getting_data_from_config = getting_data_from_json
        self.setup_user_interface(self)
        EnterData(self)
        self.enter_text.setText(set_text_for_reference)
        QMetaObject.connectSlotsByName(self)
