from PyQt5 import QtWidgets
from ui_definitions import Ui_GeneratorMainWindow, Ui_GeneratorWelcomeDialog
import sys


class GeneratorMainWindow(QtWidgets.QMainWindow, Ui_GeneratorMainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)


class GeneratorWelcomeWidget(QtWidgets.QWidget, Ui_GeneratorWelcomeDialog):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)


def main():
    print("Starting the question paper generator....")
    app = QtWidgets.QApplication(sys.argv)
    generator_main_window = GeneratorWelcomeWidget()
    generator_main_window.show()
    app.exec_()


if __name__ == '__main__':
    main()
