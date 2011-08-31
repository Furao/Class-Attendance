import os
import sys

from PyQt4 import QtCore, QtGui
from mainwindow import Ui_MainWindow
from attendb import AttendDB

class Main(QtGui.QMainWindow):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        # Setup the main window
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        # Set date to today
        self.date = QtCore.QDate.currentDate()
        self.ui.dateEdit.setDate(self.date)

        #self.dateString = self.date.toString("yyyy-MM-dd")

        # Create Attendance DB Connection Object
        self.db = AttendDB()

        # Connect signals to handlers
        self.connect(self.ui.addButton, QtCore.SIGNAL("clicked()"), self.on_student_attend)
        self.connect(self.ui.dateEdit, QtCore.SIGNAL("dateChanged(const QDate&)"), self.on_date_change)

        self.ui.attendListWidget.setSortingEnabled(True)
        self.ui.availListWidget.setSortingEnabled(True)

        self.update_views(self.date)

    def on_date_change(self, date):
        self.update_views(date)

    def update_views(self, date):
    
        self.date = date
        self.dateString = date.toString("yyyy-MM-dd")

        self.curr_students = self.db.get_attendance_for_date(self.dateString)

        self.ui.attendListWidget.clear()
        self.ui.availListWidget.clear()

        for item in self.curr_students:
            if item[1] != None:
                self.ui.attendListWidget.addItem(str(item[1]))
            else:
                self.ui.attendListWidget.addItem(str(item[2]) + ' ' + str(item[3]))

        self.student_dict = {}
        # Get all students
        self.students = self.db.get_students()
        for item in self.students:
            if item not in self.curr_students:
                if item[1] != None:
                    self.ui.availListWidget.addItem(str(item[1]))
                    self.student_dict[str(item[1])] = item[0]
                else:
                    self.ui.availListWidget.addItem(str(item[2]) + ' ' + str(item[3]))
                    self.student_dict[str(item[2]) + ' ' + str(item[3])] = item[0]

    def on_student_attend(self):
        ci = self.ui.availListWidget.currentItem() 
        print ci.text()
        print self.student_dict[str(ci.text())]
        print self.dateString
        self.db.student_attended(self.student_dict[str(ci.text())], self.dateString)
        self.update_views(self.date)

    def on_removeButton_clicked(self):
        print 'Remove Button Pressed'
    
def main():
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
