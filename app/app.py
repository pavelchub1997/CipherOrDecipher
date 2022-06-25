import datetime
import os

from CipherOrDecipher.app.ChoiseOfEncryptionAlgorithm.choise_of_encryption_algorithm import algorithm_selection
from CipherOrDecipher.app.common import generate_alphabet, GET_ABSOLUTE_PATH_FOR_JSON_FILE
from CipherOrDecipher.app.graphical_user_interface.graphical_user_interface import *
from CipherOrDecipher.app.utils.utils import utils

CONFIG = get_data_from_json("config.json")
GETTING_DATA_FOR_FORM = CONFIG["GUI"]
ALPHABET = generate_alphabet(CONFIG["alphabet"]["parameters_for_generate_russian_alphabet"])
GETTING_PATH_TO_MEDIA = os.path.join(GET_ABSOLUTE_PATH_FOR_JSON_FILE, "media")


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.getting_data_from_config = GETTING_DATA_FOR_FORM["app"]
        MainMenu(self)
        self.continue_button.clicked.connect(self.__algorithm_selection)
        self.current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.encryption_algorithms.addItems(utils)

    def __algorithm_selection(self):
        getting_encryption_algorithms_from_gui = str(self.encryption_algorithms.currentText())
        self.work_with_form = algorithm_selection.get(getting_encryption_algorithms_from_gui)(
            GETTING_DATA_FOR_FORM,
            ALPHABET,
            GETTING_PATH_TO_MEDIA,
            self.current_time
        )
        self.work_with_form.show()
        self.close()
