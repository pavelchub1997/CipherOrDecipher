from CipherOrDecipher.app.base.base import BaseEncryptedData, BaseTask
from CipherOrDecipher.app.utils.utils import utils


class EncryptedData(BaseEncryptedData):
    def __init__(self, getting_encryption_algorithms, alphabet, DECIPHER=False):
        self.getting_encryption_algorithms = getting_encryption_algorithms
        self.alphabet = alphabet
        self.DECIPHER = DECIPHER

    def execute(self):
        self.__get_encryption_algorithms().get(self.getting_encryption_algorithms)

    def __get_encryption_algorithms(self):
        return {
            utils[0]: CipherADFGVX(self.alphabet, self.DECIPHER).execute(),
            utils[1]: MethodAtbash(self.alphabet, self.DECIPHER).execute(),
            utils[2]: FourSquareCipher(self.alphabet, self.DECIPHER).execute(),
            utils[3]: Scrambling(self.alphabet, self.DECIPHER).execute(),
            utils[4]: SinglePermutationByKey(self.alphabet, self.DECIPHER).execute(),
            utils[5]: VigenereCipher(self.alphabet, self.DECIPHER).execute(),
        }


class CipherADFGVX(BaseTask, BaseEncryptedData):
    def __init__(self, alphabet, DECIPHER):
        super().__init__(alphabet, DECIPHER)

    def execute(self):
        self.decipher() if self.DECIPHER else self.cipher()

    def cipher(self):
        pass

    def decipher(self):
        pass


class MethodAtbash(BaseTask, BaseEncryptedData):
    def __init__(self, alphabet, DECIPHER):
        super().__init__(alphabet, DECIPHER)

    def execute(self):
        self.decipher() if self.DECIPHER else self.cipher()

    def cipher(self):
        pass

    def decipher(self):
        pass


class FourSquareCipher(BaseTask, BaseEncryptedData):
    def __init__(self, alphabet, DECIPHER):
        super().__init__(alphabet, DECIPHER)

    def execute(self):
        self.decipher() if self.DECIPHER else self.cipher()

    def cipher(self):
        pass

    def decipher(self):
        pass


class Scrambling(BaseTask, BaseEncryptedData):
    def __init__(self, alphabet, DECIPHER):
        super().__init__(alphabet, DECIPHER)

    def execute(self):
        self.decipher() if self.DECIPHER else self.cipher()

    def cipher(self):
        pass

    def decipher(self):
        pass


class SinglePermutationByKey(BaseTask, BaseEncryptedData):
    def __init__(self, alphabet, DECIPHER):
        super().__init__(alphabet, DECIPHER)

    def execute(self):
        self.decipher() if self.DECIPHER else self.cipher()

    def cipher(self):
        pass

    def decipher(self):
        pass


class VigenereCipher(BaseTask, BaseEncryptedData):
    def __init__(self, alphabet, DECIPHER):
        super().__init__(alphabet, DECIPHER)

    def execute(self):
        self.decipher() if self.DECIPHER else self.cipher()

    def cipher(self):
        pass

    def decipher(self):
        pass
