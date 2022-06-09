from PyQt5 import QtWidgets
from CipherOrDecipher.app.Base.BaseCipherOrDecipher import BaseCipherOrDecipher
from CipherOrDecipher.app.Base.BaseGUI import BaseGUI


class MethodAtbashGUI(QtWidgets.QMainWindow, BaseGUI):
    def __init__(self):
        super().__init__()
        self.title_window = "Шифрование методом Атбаш"
        self.next_step = False
        self.setupUi(self)


class MethodAtbash(BaseCipherOrDecipher):
    def __init__(self, text):
        super().__init__(text)

    def cipher(self):
        pass

    def decipher(self):
        pass
