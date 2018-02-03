from ui_definitions import Ui_GeneratorMainWindow
from PyQt5 import QtWidgets
import json


class GeneratorMainWindow(QtWidgets.QMainWindow, Ui_GeneratorMainWindow):

    def __init__(self, file_path):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        new_qp_file = open(file_path, "r")
        json_data = json.load(new_qp_file)
        new_qp_file.close()
        print(json_data)
