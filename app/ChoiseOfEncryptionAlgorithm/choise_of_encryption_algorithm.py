from PyQt5 import QtWidgets
from CipherOrDecipher.app.utils.utils import utils
from CipherOrDecipher.app.ChoiseOfEncryptionAlgorithm.EncryptionAlgorithms.ADFGVXCipher.ADFGVX_cipher \
    import CipherADFGVX
from CipherOrDecipher.app.ChoiseOfEncryptionAlgorithm.EncryptionAlgorithms.AtbashMethod.atbash_method \
    import MethodAtbash
from CipherOrDecipher.app.ChoiseOfEncryptionAlgorithm.EncryptionAlgorithms.FourSquareCipher.four_square_cipher \
    import FourSquareCipher
from CipherOrDecipher.app.ChoiseOfEncryptionAlgorithm.EncryptionAlgorithms.Scrambling.scrambling import Scrambling
from CipherOrDecipher.app.ChoiseOfEncryptionAlgorithm.EncryptionAlgorithms.SinglePermutationByKey.\
    single_permutation_by_key import SinglePermutationByKey
from CipherOrDecipher.app.ChoiseOfEncryptionAlgorithm.EncryptionAlgorithms.VigenereCipher.vigenere_cipher \
    import VigenereCipher

CONST_APP = QtWidgets.QApplication([])

algorithm_selection = {
    utils[0]: lambda getting_data_from_json, alphabet:
    CipherADFGVX(utils[0], getting_data_from_json, alphabet),
    utils[1]: lambda getting_data_from_json, alphabet:
    MethodAtbash(utils[1], getting_data_from_json, alphabet),
    utils[2]: lambda getting_data_from_json, alphabet:
    FourSquareCipher(utils[2], getting_data_from_json, alphabet),
    utils[3]: lambda getting_data_from_json, alphabet:
    Scrambling(utils[3], getting_data_from_json, alphabet),
    utils[4]: lambda getting_data_from_json, alphabet:
    SinglePermutationByKey(utils[4], getting_data_from_json, alphabet),
    utils[5]: lambda getting_data_from_json, alphabet:
    VigenereCipher(utils[5], getting_data_from_json, alphabet),
}
