import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QPushButton, QDesktopWidget


class BaseGUI(QWidget):

    def __init__(self, title_window=''):
        super().__init__()
        self.title_window = title_window
        self.initUI()

    def initUI(self):
        self._settings_window()
        self._shutdown()
        self.show()

    def _settings_window(self):
        self.resize(350, 400)
        self._center()
        self.setWindowTitle(self.title_window)
        return self

    def _center(self):
        geometry_main_window = self.frameGeometry()
        center_point_desktop = QDesktopWidget().availableGeometry().center()
        geometry_main_window.moveCenter(center_point_desktop)
        self.move(geometry_main_window.topLeft())
        return self

    def _shutdown(self):
        shutdown = QPushButton('Завершение работы', self)
        shutdown.clicked.connect(self._quit)
        shutdown.resize(shutdown.sizeHint())
        shutdown.move(100, 350)

    def _quit(self):
        question = QMessageBox.question(self, "Вы уверены, что хотите завершить работу программы?",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if question == QMessageBox.Yes:
            sys.exit(0)

