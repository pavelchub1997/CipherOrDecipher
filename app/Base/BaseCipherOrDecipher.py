from abc import abstractmethod, ABC


class BaseCipherOrDecipher(ABC):
    @abstractmethod
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def cipher(self):
        pass

    @abstractmethod
    def decipher(self):
        pass
