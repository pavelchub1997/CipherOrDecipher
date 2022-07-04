import os

from CipherOrDecipher.app.base.base import BaseDataWork
from CipherOrDecipher.app.common.common import GET_ABSOLUTE_PATH_FOR_JSON_FILE, generate_alphabet
from CipherOrDecipher.app.data_work.encrypted_data.encrypted_data import EncryptedData
from CipherOrDecipher.app.graphical_user_interface.graphical_user_interface \
    import WindowForEncryptionOrDecryptionData
from CipherOrDecipher.app.data_work.help import Help

GETTING_PATH_TO_MEDIA = os.path.join(GET_ABSOLUTE_PATH_FOR_JSON_FILE, "media")


class DataWork(BaseDataWork):
    def __init__(self, getting_encryption_algorithms, getting_data_from_config):
        super().__init__(getting_encryption_algorithms, getting_data_from_config)
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
        EncryptedData(self.getting_encryption_algorithms, self.alphabet).execute()

    def __decipher(self):
        EncryptedData(self.getting_encryption_algorithms, self.alphabet, DECIPHER=True).execute()
