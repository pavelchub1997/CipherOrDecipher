import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QPushButton, QDesktopWidget, QComboBox
from PyQt5.QtCore import QMetaObject


class BaseGUI(object):

    def setupUi(self, base_gui):
        self._settings_window(base_gui)
        self._next_step(base_gui) if base_gui.next_step else self._comeback(base_gui)
        self.shutdown = self._forming_button(base_gui, 'Завершение работы', 100, 350)
        self.shutdown.clicked.connect(self._forming_quit)
        QMetaObject.connectSlotsByName(base_gui)

    def _settings_window(self, base_gui):
        base_gui.resize(350, 400)
        self._center(base_gui)
        base_gui.setWindowTitle(base_gui.title_window)

    def _center(self, base_gui):
        self.geometry_main_window = QWidget.frameGeometry(base_gui)
        self.center_point_desktop = QDesktopWidget().availableGeometry().center()
        self.geometry_main_window.moveCenter(self.center_point_desktop)
        base_gui.move(self.geometry_main_window.topLeft())

    def _next_step(self, base_gui):
        self.encryption_algorithms = QComboBox(base_gui)
        self.encryption_algorithms.move(75, 150)

    def _comeback(self, base_gui):
        self.cipher = self._forming_button(base_gui, 'Шифровать', 50, 300)
        self.decipher = self._forming_button(base_gui, 'Дешифровать', 200, 300)

    def _forming_button(self, base_gui, title="", coord_x=int(0), coord_y=int(0)) -> QPushButton:
        self.forming_button = QPushButton(title, base_gui)
        self.forming_button.resize(self.forming_button.sizeHint())
        self.forming_button.move(coord_x, coord_y)
        return self.forming_button

    def _forming_quit(self):
        sys.exit(0)
