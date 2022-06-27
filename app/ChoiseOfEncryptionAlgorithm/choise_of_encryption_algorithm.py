algorithm_selection = {
    utils[0]: lambda getting_data_from_json, alphabet, path_to_media, current_time:
    CipherADFGVX(utils[0], getting_data_from_json, alphabet, path_to_media, current_time),
    utils[1]: lambda getting_data_from_json, alphabet, path_to_media, current_time:
    MethodAtbash(utils[1], getting_data_from_json, alphabet, path_to_media, current_time),
    utils[2]: lambda getting_data_from_json, alphabet, path_to_media, current_time:
    FourSquareCipher(utils[2], getting_data_from_json, alphabet, path_to_media, current_time),
    utils[3]: lambda getting_data_from_json, alphabet, path_to_media, current_time:
    Scrambling(utils[3], getting_data_from_json, alphabet, path_to_media, current_time),
    utils[4]: lambda getting_data_from_json, alphabet, path_to_media, current_time:
    SinglePermutationByKey(utils[4], getting_data_from_json, alphabet, path_to_media, current_time),
    utils[5]: lambda getting_data_from_json, alphabet, path_to_media, current_time:
    VigenereCipher(utils[5], getting_data_from_json, alphabet, path_to_media, current_time),
}
