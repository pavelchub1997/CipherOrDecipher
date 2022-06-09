from PyQt5.QtWidgets import QMainWindow
from CipherOrDecipher.app.Base.BaseGUI import BaseGUI
from CipherOrDecipher.app.utils.utils import utils
from CipherOrDecipher.app.ChoiseOfEncryptionAlgorithm.choise_of_encryption_algorithm import algorithm_selection


class App(QMainWindow, BaseGUI):
    # TODO: replace index algorithm_selection text combobox
    def __init__(self):
        super().__init__()
        self.next_step = True
        self.title_window = "Главное окно программы"
        self.setupUi(self)
        self.encryption_algorithms.addItems(utils)
        super()._forming_button(self, 'Продолжить', 125, 300).clicked.connect(self._algorithm_selection)

    def _algorithm_selection(self):
        find = str(self.encryption_algorithms.currentText())
        algorithm_selection.get(find).show()
