from PyQt5.QtWidgets import QMainWindow


class BaseGraphicalUserInterface(object):

    def setup_user_interface(self, obj):
        pass


class BaseDataWork(QMainWindow):

    def _comeback(self):
        from CipherOrDecipher.app.app import App
        self.main_menu = App()
        self.main_menu.show()
        self.close()


class BaseEncryptedData:

    def execute(self):
        pass


class BaseDecryptedData:

    def execute(self):
        pass


class BaseHelp(QMainWindow):

    def _get_reference(self):
        pass
