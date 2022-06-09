from PyQt5 import QtWidgets
from CipherOrDecipher.app.utils.utils import utils
from CipherOrDecipher.app.ChoiseOfEncryptionAlgorithm.EncryptionAlgorithms.ADFGVXCipher.ADFGVX_cipher \
    import CipherADFGVXGUI
from CipherOrDecipher.app.ChoiseOfEncryptionAlgorithm.EncryptionAlgorithms.AtbashMethod.atbash_method \
    import MethodAtbashGUI
from CipherOrDecipher.app.ChoiseOfEncryptionAlgorithm.EncryptionAlgorithms.FourSquareCipher.four_square_cipher \
    import FourSquareCipherGUI
from CipherOrDecipher.app.ChoiseOfEncryptionAlgorithm.EncryptionAlgorithms.Scrambling.scrambling import ScramblingGUI
from CipherOrDecipher.app.ChoiseOfEncryptionAlgorithm.EncryptionAlgorithms.SinglePermutationByKey.\
    single_permutation_by_key import SinglePermutationByKeyGUI
from CipherOrDecipher.app.ChoiseOfEncryptionAlgorithm.EncryptionAlgorithms.VigenereCipher.vigenere_cipher \
    import VigenereCipherGUI

CONST_APP = QtWidgets.QApplication([])

algorithm_selection = {
    utils[0]: CipherADFGVXGUI(),
    utils[1]: MethodAtbashGUI(),
    utils[2]: FourSquareCipherGUI(),
    utils[3]: ScramblingGUI(),
    utils[4]: SinglePermutationByKeyGUI(),
    utils[5]: VigenereCipherGUI(),
}
