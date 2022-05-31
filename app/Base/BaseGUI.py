from PyQt5.QtWidgets import QWidget, QMessageBox, QPushButton
from PyQt5.QtCore import QCoreApplication


class BaseGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self._shutdown()

    def _shutdown(self):
        shutdown = QPushButton('Завершение работы', self)
        shutdown.clicked.connect(QCoreApplication.instance().quit)
        shutdown.resize(shutdown.sizeHint())
        shutdown.move(50, 50)

