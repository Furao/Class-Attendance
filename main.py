import os
import sys

from PyQt4 import QtCore, QtGui
from mainwindow import Ui_MainWindow

class Main(QtGui.QMainWindow):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

def main():
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
