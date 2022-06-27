import os

from CipherOrDecipher.app.base.base import BaseDataWork, BaseEncryptedData, BaseDecryptedData
from CipherOrDecipher.app.common.common import GET_ABSOLUTE_PATH_FOR_JSON_FILE, generate_alphabet
from CipherOrDecipher.app.graphical_user_interface.graphical_user_interface \
    import WindowForEncryptionOrDecryptionData
from CipherOrDecipher.app.encryption_or_decryption_data.help import Help

GETTING_PATH_TO_MEDIA = os.path.join(GET_ABSOLUTE_PATH_FOR_JSON_FILE, "media")


class DataWork(BaseDataWork):
    def __init__(self, getting_encryption_algorithms, getting_data_from_config):
        super().__init__()
        self.getting_encryption_algorithms = getting_encryption_algorithms
        self.getting_data_from_config = getting_data_from_config["GUI"]
        self.alphabet = generate_alphabet(
            getting_data_from_config["alphabet"]["parameters_for_generate_russian_alphabet"]
        )
        WindowForEncryptionOrDecryptionData(self)
        self.help = Help(self, getting_data_from_config["GUI"])
        self.help_button.clicked.connect(self.help.get_reference)
        self.cipher_button.clicked.connect(self.__cipher)
        self.decipher_button.clicked.connect(self.__decipher)
        self.comeback.clicked.connect(self._comeback)

    def __cipher(self):
        EncryptedData(self.getting_encryption_algorithms).execute()

    def __decipher(self):
        DecryptedData(self.getting_encryption_algorithms).execute()


class EncryptedData(BaseEncryptedData):
    def __init__(self, getting_encryption_algorithms):
        self.getting_encryption_algorithms = getting_encryption_algorithms

    def execute(self):
        pass


class DecryptedData(BaseDecryptedData):
    def __init__(self, getting_encryption_algorithms):
        self.getting_encryption_algorithms = getting_encryption_algorithms

    def execute(self):
        pass
