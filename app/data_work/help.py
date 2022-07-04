from CipherOrDecipher.app.base.base import BaseHelp
from CipherOrDecipher.app.graphical_user_interface.graphical_user_interface import ReferenceGUI
from CipherOrDecipher.app.common.common import get_data_from_json

GETTING_INFO_ABOUT_REFERENCE = get_data_from_json("referenceInformation.json")


class Help(BaseHelp):
    def __init__(self, obj_cls, getting_data_from_config):
        super().__init__()
        self.getting_data_from_config = getting_data_from_config["reference"]
        self.getting_encryption_algorithms = obj_cls.getting_encryption_algorithms

    def get_reference(self):
        ReferenceGUI(self)
        self.enter_text.setText(GETTING_INFO_ABOUT_REFERENCE[self.getting_encryption_algorithms])
        self.show()
