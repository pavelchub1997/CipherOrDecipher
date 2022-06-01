from PyQt5.QtWidgets import QComboBox
from .Base.BaseGUI import BaseGUI
from .utils.utils import utils
from .ChoiseOfEncryptionAlgorithm.choise_of_encryption_algorithm import algorithm_selection


class App(BaseGUI):
    def __init__(self):
        super().__init__(title_window="Главное окно программы")
        self.initUI()

    def initUI(self):
        self._algorithm_selection()
        super().initUI()

    def _algorithm_selection(self):
        encryption_algorithms = QComboBox(self)
        encryption_algorithms.addItems(*utils)
        encryption_algorithms.move(100, 150)
        self.lbl.move(100, 250)
        # encryption_algorithms.activated[str].connect(algorithm_selection)
