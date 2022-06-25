from CipherOrDecipher.app.base.base import BaseCipherOrDecipher
from CipherOrDecipher.app.graphical_user_interface.graphical_user_interface import BaseEncryptionAlgorithms


class SinglePermutationByKey(BaseEncryptionAlgorithms, BaseCipherOrDecipher):
    def __init__(self, key_for_getting_reference, getting_data_from_json, alphabet, path_to_media, current_time):
        super().__init__(getting_data_from_config=getting_data_from_json[key_for_getting_reference])
        self.getting_data_from_config_for_reference = getting_data_from_json
        self.alphabet = alphabet
        self.path_to_media = path_to_media
        self.current_time = current_time
        self.key_for_getting_reference = key_for_getting_reference
        self.help_button.clicked.connect(self._forming_reference)
        self.cipher_button.clicked.connect(self.cipher)
        self.decipher_button.clicked.connect(self.decipher)
        self.comeback.clicked.connect(self._comeback)

    def cipher(self):
        pass

    def decipher(self):
        pass
