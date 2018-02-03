from ui_definitions import Ui_GeneratorMainWindow
from PyQt5 import QtWidgets
from helper_widgets import NewQPWidget
import json


class GeneratorMainWindow(QtWidgets.QMainWindow, Ui_GeneratorMainWindow):

    def __init__(self, file_path=''):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        if file_path == '':
            QtWidgets.QMessageBox.critical(self, 'Error Creating', 'Unable to open the file, exiting !',
                                           QtWidgets.QMessageBox.Ok)
            return

        new_qp_file = open(file_path, "r")
        json_data = json.load(new_qp_file)
        new_qp_file.close()
        print("Loaded data: " + json_data)

        # Connect actions to slots
        self.actionNew_QP.triggered.connect(self.create_file_action)


        # Slots:
    def create_file_action(self):

        create_file_dialog = NewQPWidget()
        create_file_dialog.exec_()

        

