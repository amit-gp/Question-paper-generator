from PyQt5 import QtWidgets
from ui_definitions import Ui_GeneratorMainWindow, Ui_GeneratorWelcomeDialog
from helper_widgets import NewQPWidget
import sys


class GeneratorMainWindow(QtWidgets.QMainWindow, Ui_GeneratorMainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)


class GeneratorWelcomeWidget(QtWidgets.QWidget, Ui_GeneratorWelcomeDialog):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.create_new_qp_clicked)
        self.pushButton.clicked.connect(self.settings_clicked)
        self.openPushButton.clicked.connect(self.open_new_qp_clicked)

    def create_new_qp_clicked(self):
        self.new_qp_win = NewQPWidget()
        self.new_qp_win.show()

    def open_new_qp_clicked(self):
        pass

    def settings_clicked(self):
        pass


def main():
    print("Starting the question paper generator....")
    app = QtWidgets.QApplication(sys.argv)
    start_window = GeneratorWelcomeWidget()
    start_window.show()
    app.exec_()


if __name__ == '__main__':
    main()
