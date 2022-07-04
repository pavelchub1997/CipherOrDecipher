from abc import ABC, abstractmethod
from datetime import datetime

from PyQt5.QtWidgets import QMainWindow


class BaseGraphicalUserInterface(object):

    def setup_user_interface(self, obj):
        pass


class BaseDataWork(QMainWindow):
    def __init__(self, getting_encryption_algorithms, getting_data_from_config):
        super().__init__()
        self.getting_encryption_algorithms = getting_encryption_algorithms
        self.getting_data_from_config = getting_data_from_config["GUI"]

    def _comeback(self):
        from CipherOrDecipher.app.app import App
        self.main_menu = App()
        self.main_menu.show()
        self.close()


class BaseHelp(QMainWindow):

    def get_reference(self):
        pass


class BaseEncryptedData(ABC):

    @abstractmethod
    def execute(self):
        pass


class BaseTask:
    @abstractmethod
    def __init__(self, alphabet, DECIPHER):
        self.alphabet = alphabet
        self.current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.DECIPHER = DECIPHER

    @abstractmethod
    def cipher(self):
        pass

    @abstractmethod
    def decipher(self):
        pass
