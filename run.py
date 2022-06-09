import sys
from PyQt5 import QtWidgets
from CipherOrDecipher.app.app import App


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = App()
    main_window.show()
    app.exec()
