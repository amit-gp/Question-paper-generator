from PyQt5 import QtWidgets
from ui_definitions import Ui_QPDWelcomeDialog
from helper_widgets import NewQPWidget
import json


class QPDEditor(QtWidgets.QMainWindow):

        def __init__(self, file_path=''):
            super(self.__class__, self).__init__()
            if not self.load_qpd(file_path):
                return

        def load_qpd(self, file_path):
            if file_path == '':
                QtWidgets.QMessageBox.critical(self, 'Error Creating', 'Unable to open the file, exiting !',
                                               QtWidgets.QMessageBox.Ok)
                return 0

            new_qp_file = open(file_path, "r")
            json_data = json.load(new_qp_file)
            new_qp_file.close()
            print("Loaded data: " + str(json_data))
            # self.load_gui_values(json_data)
            return 1


class QPDWelcomeDialog(QtWidgets.QDialog, Ui_QPDWelcomeDialog):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.create_push_button.clicked.connect(self.create_clicked)
        self.open_push_button.clicked.connect(self.open_clicked)

    def create_clicked(self):
        new_qp_win = NewQPWidget('.qpd')
        if not new_qp_win.exec_():
            return

        self.gen_win = QPDEditor(new_qp_win.new_file)
        self.gen_win.show()
        self.close()

    def open_clicked(self):
        pass