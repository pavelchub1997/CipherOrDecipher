from PyQt5.QtWidgets import QMainWindow

from CipherOrDecipher.app.Base.BaseGUI import BaseGUI
from CipherOrDecipher.app.utils.utils import utils
from CipherOrDecipher.app.ChoiseOfEncryptionAlgorithm.choise_of_encryption_algorithm import algorithm_selection
from CipherOrDecipher.app.common import get_data_from_json

GETTING_DATA_FOR_FORM = get_data_from_json("config_file_for_GUI.json")


class App(QMainWindow, BaseGUI):
    def __init__(self):
        super().__init__()
        self.choise_of_encryption_algorithm = True
        self.getting_data_from_config = GETTING_DATA_FOR_FORM["app"]
        super()._forming_button(
            self,
            **self.getting_data_from_config["parameters_button_for_continue_work"]
        ).clicked.connect(self._algorithm_selection)
        self.setupUi(self)
        self.encryption_algorithms.addItems(utils)

    def _algorithm_selection(self):
        getting_encryption_algorithms_from_gui = str(self.encryption_algorithms.currentText())
        self.work_with_form = algorithm_selection.get(getting_encryption_algorithms_from_gui)(GETTING_DATA_FOR_FORM)
        self.work_with_form.show()
        self.close()
