from ui_definitions import Ui_GeneratorMainWindow
from PyQt5 import QtWidgets
from helper_widgets import NewQPWidget, OpenQPWidget
import json


class GeneratorMainWindow(QtWidgets.QMainWindow, Ui_GeneratorMainWindow):

    def __init__(self, file_path=''):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        if not self.load_qp_data(file_path):
            return
        # Connect actions to slots
        self.actionNew_QP.triggered.connect(self.create_file_action)
        self.actionLoad_QP.triggered.connect(self.open_file_action)

        # Slots:
    def create_file_action(self):
        create_file_dialog = NewQPWidget()
        if create_file_dialog.exec_() == 0:
            return
        self.load_qp_data(create_file_dialog.new_file)

    def open_file_action(self):
        open_file_dialog = OpenQPWidget()
        if not open_file_dialog.open_file:
            return
        self.load_qp_data(open_file_dialog.open_file)

    def load_qp_data(self, file_path):
        if file_path == '':
            QtWidgets.QMessageBox.critical(self, 'Error Creating', 'Unable to open the file, exiting !',
                                           QtWidgets.QMessageBox.Ok)
            return 0

        new_qp_file = open(file_path, "r")
        json_data = json.load(new_qp_file)
        new_qp_file.close()
        print("Loaded data: " + str(json_data))
        self.load_gui_values(json_data)
        return 1

    def load_gui_values(self, json_data):

        self.qp_code_line_edit.setText(json_data['qp_code'])
        self.exam_name_line_edit.setText(json_data['exam_name'])
        self.program_line_edit.setText(json_data['program'])
        self.course_code_line_edit.setText(json_data['course_code'])
        self.marks_spin_box.setValue(json_data['max_marks'])
        self.exam_date_edit.setDate()