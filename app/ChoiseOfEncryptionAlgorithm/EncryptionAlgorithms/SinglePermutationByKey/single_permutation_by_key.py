from CipherOrDecipher.app.Base.BaseCipherOrDecipher import BaseCipherOrDecipher


class SinglePermutationByKey(BaseCipherOrDecipher):
    def __init__(self, text):
        super().__init__(text)

    def cipher(self):
        pass

    def decipher(self):
        pass