import os
import sys

from PyQt4 import QtCore, QtGui
from mainwindow import Ui_MainWindow
from attendb import AttenDB

class Main(QtGui.QMainWindow):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        # Setup the main window
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        # Set date to today
        today = QtCore.QDate.currentDate()
        self.ui.dateEdit.setDate(today)

        # Create Attendance DB Connection Object
        self.db = AttendDB()

        # Get all students
        self.students = self.db.get_students()
        for item in student:
            print item

    def on_addButton_clicked(self):
        print 'Add Button Pressed'

    def on_removeButton_clicked(self):
        print 'Remove Button Pressed'
    
def main():
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
