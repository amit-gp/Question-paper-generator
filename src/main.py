from PyQt5 import QtWidgets
from main_window import GeneratorMainWindow
from helper_widgets import NewQPWidget
import sys
from ui_definitions import Ui_GeneratorWelcomeDialog


class GeneratorWelcomeWidget(QtWidgets.QWidget, Ui_GeneratorWelcomeDialog):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.create_new_qp_clicked)
        self.pushButton.clicked.connect(self.settings_clicked)
        self.openPushButton.clicked.connect(self.open_new_qp_clicked)

    def create_new_qp_clicked(self):
        new_qp_win = NewQPWidget()
        new_qp_win.exec_()

        self.gen_win = GeneratorMainWindow(new_qp_win.new_file)
        self.gen_win.show()
        self.close()

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
