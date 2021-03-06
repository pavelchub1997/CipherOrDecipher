import datetime

from PyQt5.QtWidgets import QMainWindow

from CipherOrDecipher.app.encryption_or_decryption_data.encryption_or_decryption_data import DataWork
from CipherOrDecipher.app.common.common import get_data_from_json
from CipherOrDecipher.app.graphical_user_interface.graphical_user_interface import MainMenu
from CipherOrDecipher.app.utils.utils import utils

CONFIG = get_data_from_json("config.json")


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.getting_data_from_config = CONFIG["GUI"]["app"]
        MainMenu(self)
        self.continue_button.clicked.connect(self.__algorithm_selection)
        self.current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.encryption_algorithms.addItems(utils)

    def __algorithm_selection(self):
        self.work_with_form = DataWork(str(self.encryption_algorithms.currentText()), CONFIG)
        self.work_with_form.show()
        self.close()
