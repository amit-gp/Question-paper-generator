from ui_definitions import Ui_GeneratorMainWindow
from PyQt5 import QtWidgets, QtCore
from helper_widgets import NewQPWidget, OpenQPWidget
from qpd_editor import QPDWelcomeDialog
from PyQt5.QtCore import QDate
from reportlab.pdfgen import canvas
import json


class GeneratorMainWindow(QtWidgets.QMainWindow, Ui_GeneratorMainWindow):

    def __init__(self, file_path=''):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        if not self.load_qp_data(file_path):
            return

        self.file_path = file_path
        # Connect actions to slots
        self.actionNew_QP.triggered.connect(self.create_file_action)
        self.actionLoad_QP.triggered.connect(self.open_file_action)
        self.actionSave_QP.triggered.connect(self.save_file_action)
        self.GenQpPushButton.clicked.connect(self.generate_qp)
        self.qp_data_tool_button.clicked.connect(self.load_qp_data_tool_clicked)
        self.LoadQpdPushButton.clicked.connect(self.qpd_open_clicked)

    # Slots:

    def qpd_open_clicked(self):

        # Loading the listview..
        self.load_qpd_data(self.qp_data_line_edit.text())

        self.qpdwelcome = QPDWelcomeDialog()
        self.qpdwelcome.show()

    def load_qp_data_tool_clicked(self):
        self.qp_data_file = QtWidgets.QFileDialog.getOpenFileName(self, 'Open Question paper data',
                                                                  str(QtCore.QStandardPaths.DocumentsLocation),
                                                                  'Question Paper Data (*.qpd)')[0]
        if not self.qp_data_file:
            return
        self.qp_data_line_edit.setText(self.qp_data_file)

    def save_file_action(self):
        sv_file = open(self.file_path, 'w')
        json.dump(self.get_json_data_from_fields(), sv_file, ensure_ascii=False)
        print("\nSaving file to: %s", self.file_path)
        self.statusbar.showMessage("Saved file to :" + self.file_path, 3000)

    def get_json_data_from_fields(self):
        json_dict = dict(exam_name=self.exam_name_line_edit.text(),
                         course_code=self.course_code_line_edit.text(),
                         qp_code=self.qp_code_line_edit.text(),
                         program=self.program_line_edit.text(),
                         max_marks=self.marks_spin_box.value(),
                         date=QDate.toString(self.exam_date_edit.date(), 'ddMMyyyy'),
                         semester=self.sem_spin_box.value(),
                         duration=self.duration_spin_box.value(),
                         num_parts=self.num_parts_spin_box.value(),
                         qp_data=self.qp_data_line_edit.text())
        return json_dict

    def create_file_action(self):
        create_file_dialog = NewQPWidget()
        if create_file_dialog.exec_() == 0:
            return
        self.load_qp_data(create_file_dialog.new_file)

    def generate_qp(self):
        if not self.qp_data_line_edit.text():
            QtWidgets.QMessageBox.critical(self, 'Error', 'Question Bank data must be provided.',
                                           QtWidgets.QMessageBox.Ok)
            return

        canv = canvas.Canvas(self.exam_name_line_edit.text())
        canv.setLineWidth(.3)
        canv.setFont('Helvetica', 12)

        canv.drawString(30, 750, 'Exam Name: ' + self.exam_name_line_edit.text())
        canv.drawString(30, 735, 'Course: ' + self.course_code_line_edit.text())
        canv.drawString(30, 720, 'Paper Code: ' + self.qp_code_line_edit.text())
        canv.drawString(30, 705, 'Semester: ' + str(self.sem_spin_box.value()))

        canv.drawString(450, 750, "Date: " + QDate.toString(self.exam_date_edit.date(), 'dd/MM/yyyy'))
        canv.drawString(450, 735, "Max Marks: " + str(self.marks_spin_box.value()))
        canv.drawString(450, 720, "Program: " + self.program_line_edit.text())
        canv.drawString(450, 705, "Duration: " + str(self.duration_spin_box.value()) + " mins")

        # self.qpd_print_num_vals = 0
        # self.qpd_print_vals = {}
        # for key, val in self.qpd_json.items():
        #     # So that the keys can be printed in ascending order
        #     self.qpd_print_vals[key] = val
        #     self.qpd_print_num_vals += 1
        #
        # print(self.qpd_print_num_vals)
        # print(self.qpd_print_vals)
        # for i in range(1, self.qpd_print_num_vals + 1):
        #     canv.drawString(30, 650 + (15 * int(i)),
        #                     str(i) + ". " + str(self.qpd_print_vals[str(i)]["QUESTION"]) + "\t\t[ " + str(
        #                         self.qpd_print_vals[str(i)]["MARKS"])


        for key, val in self.qpd_json.items():
            canv.drawString(30, 620 + (20 * int(key)),
                 "Q. " + str(val["QUESTION"]) + "     [ " + str(
                                val["MARKS"]) + "]")

        canv.save()

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)

        msg.setText("Success")
        msg.setInformativeText("The Question paper has been generated !")
        msg.setWindowTitle("Done")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        # msg.buttonClicked.connect(msgbtn)

        retval = msg.exec_()

    def open_file_action(self):
        open_file_dialog = OpenQPWidget()
        if not open_file_dialog.open_file:
            return
        self.load_qp_data(open_file_dialog.open_file)

    def load_qpd_data(self, file_path):
        if file_path == '':
            QtWidgets.QMessageBox.critical(self, 'Error Creating', 'Unable to open the qpd file, exiting !',
                                           QtWidgets.QMessageBox.Ok)
            return 0

        new_qp_file = open(file_path, "r")
        json_data = json.load(new_qp_file)
        new_qp_file.close()
        print("Loaded data: " + str(json_data))
        self.QpdListView.clear()
        for key, value in json_data.items():
            print(value["QUESTION"])
            self.QpdListView.addItem(str(value['QUESTION']))
        self.qpd_json = json_data
        return 1

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
        self.exam_date_edit.setDate(QDate.fromString(json_data['date'], 'ddMMyyyy'))
        self.sem_spin_box.setValue(json_data['semester'])
        self.duration_spin_box.setValue(json_data['duration'])
        self.num_parts_spin_box.setValue(json_data['num_parts'])
        self.qp_data_line_edit.setText(json_data['qp_data'])
