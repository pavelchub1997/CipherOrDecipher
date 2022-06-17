from CipherOrDecipher.app.Base.BaseCipherOrDecipher import BaseCipherOrDecipher
from CipherOrDecipher.app.Base.BaseGUI import BaseEncryptionAlgorithms


class VigenereCipher(BaseEncryptionAlgorithms, BaseCipherOrDecipher):
    def __init__(self, key_for_getting_reference, getting_data_from_json):
        super().__init__(
            choise_of_encryption_algorithm=False,
            key_is_needed=True,
            getting_data_from_config=getting_data_from_json[key_for_getting_reference],
        )
        self.getting_data_from_config_for_reference = getting_data_from_json
        self.key_for_getting_reference = key_for_getting_reference
        self.reference.clicked.connect(self._forming_reference)
        self.process_cipher.clicked.connect(self.cipher)
        self.process_decipher.clicked.connect(self.decipher)
        self.comeback.clicked.connect(self._comeback)

    def cipher(self):
        pass

    def decipher(self):
        pass
