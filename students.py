from PyQt4 import QtCore, QtGui

from studentswindow import Ui_studentsDialog

class Students(QtGui.QDialog):

    def __init__(self):
        QtGui.QDialog.__init__(self)

        # setup
        self.dialog = Ui_studentsDialog()
        self.dialog.setupUi(self)
