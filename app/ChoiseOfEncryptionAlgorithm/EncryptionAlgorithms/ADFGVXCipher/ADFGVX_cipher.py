from PyQt5 import QtWidgets

from CipherOrDecipher.app.Base.BaseCipherOrDecipher import BaseCipherOrDecipher
from CipherOrDecipher.app.Base.BaseGUI import BaseGUI


class CipherADFGVXGUI(QtWidgets.QMainWindow, BaseGUI):
    def __init__(self):
        super().__init__()
        self.title_window = "Шифрование методом ADFGVX"
        self.next_step = False
        self.setupUi(self)
        # self.cipher.clicked.connect(CipherADFGVX(self.text.text()).cipher)
        # self.decipher.connect.connect(CipherADFGVX(self.text.text()).decipher)


class CipherADFGVX(BaseCipherOrDecipher):
    def __init__(self, text):
        super().__init__(text)

    def cipher(self):
        pass

    def decipher(self):
        pass
