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
    utils[0]: lambda getting_data_from_json: CipherADFGVX(utils[0], getting_data_from_json),
    utils[1]: lambda getting_data_from_json: MethodAtbash(utils[1], getting_data_from_json),
    utils[2]: lambda getting_data_from_json: FourSquareCipher(utils[2], getting_data_from_json),
    utils[3]: lambda getting_data_from_json: Scrambling(utils[3], getting_data_from_json),
    utils[4]: lambda getting_data_from_json: SinglePermutationByKey(utils[4], getting_data_from_json),
    utils[5]: lambda getting_data_from_json: VigenereCipher(utils[5], getting_data_from_json),
}
