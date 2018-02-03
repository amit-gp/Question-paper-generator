from PyQt5 import QtWidgets, QtCore
from ui_definitions import Ui_NewQPDialog
import os.path
from global_vars import GlobalVars
import json
from main_window import GeneratorMainWindow


class NewQPWidget(QtWidgets.QDialog, Ui_NewQPDialog):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self._initialize_defaults()
        self.gv = GlobalVars()

        # Connecting the signals and slots
        self.create_qp_push_button.clicked.connect(self.create_qp_clicked)
        self.cancel_push_button.clicked.connect(self.cancel_qp_clicked)
        self.qp_path_tool_button.clicked.connect(self.qp_path_clicked)
        self.qp_filename_line_edit.textChanged.connect(self.filename_line_edit_changed)
        self.qp_path_line_edit.textChanged.connect(self.path_line_edit_changed)

    #    Slots:
    def filename_line_edit_changed(self):
        self.qp_filename = self.qp_filename_line_edit.text()

    def path_line_edit_changed(self):
        self.qp_path = self.qp_path_line_edit.text()

    def create_qp_clicked(self):
        # Checking to see if the values are valid
        if not (self.qp_path_line_edit.text()) or not (self.qp_filename_line_edit.text()):
            QtWidgets.QMessageBox.critical(self, 'Error Creating', 'The input fields are invalid', QtWidgets.QMessageBox.Ok)
            return
        if not (self.get_file_extension(self.qp_filename_line_edit.text()) == '.qp'):
            self.qp_filename = self.qp_filename + '.qp'

        self.setEnabled(False)
        # Creating a new instance of GeneratorMainWindow, after creating and loading the file
        new_file = ''
        if os.name == 'posix':
            new_file = QtCore.QDir(self.qp_path + '/' +  self.qp_filename).path()
        elif os.name == 'nt':
            new_file = QtCore.QDir(self.qp_path + '\\' + self.qp_filename).path()
        print("Creating new qp file " + new_file)
        q_file = QtCore.QFile(new_file)
        if not q_file.open(QtCore.QFile.ReadWrite):
            QtWidgets.QMessageBox.critical(self, 'Error Creating', 'Unable to create the file !',
                                           QtWidgets.QMessageBox.Ok)
            return
        q_file.close()
        self.new_qp_full_path = new_file
        #print(self.gv.default_qp_values)
        file = open(new_file, "w", encoding="utf-8")
        json.dump(self.gv.default_qp_values, file)
        file.close()
        #Created the file with default contents
        self.close()

        # Load the main window
        self.main_win = GeneratorMainWindow(self.new_qp_full_path)
        self.main_win.show()

    def cancel_qp_clicked(self):
        self.close()

    def qp_path_clicked(self):
        self.qp_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Choose path', self.qp_path,
                                    QtWidgets.QFileDialog.ShowDirsOnly | QtWidgets.QFileDialog.DontResolveSymlinks)
        self.qp_path_line_edit.setText(self.qp_path)

    #   Class methods:

    def _initialize_defaults(self):
        self.qp_path = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.DocumentsLocation)
        self.qp_path_line_edit.setText(self.qp_path)

        self.qp_filename = 'untitled.qp'
        self.qp_filename_line_edit.setText(self.qp_filename)

    def get_file_extension(self, file):
        return os.path.splitext(file)[1]
