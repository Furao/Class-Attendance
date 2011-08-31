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

        # Date format for SQLite
        self.date_format = "yyyy-MM-dd"

        # Used to remember the Students Id
        self.student_dict = {}
        
        # Create Attendance DB Connection Object
        self.db = AttendDB()

        # Connect signals to handlers
        self.connect(self.ui.addButton, QtCore.SIGNAL("clicked()"), \
                self.on_add_clicked)
        self.connect(self.ui.removeButton, QtCore.SIGNAL("clicked()"), \
                self.on_remove_clicked)
        self.connect(self.ui.dateEdit, \
                QtCore.SIGNAL("dateChanged(const QDate&)"), \
                self.on_date_change)

        # Enable sorting on the list widgets
        self.ui.attendListWidget.setSortingEnabled(True)
        self.ui.availListWidget.setSortingEnabled(True)

        # Update the lists to reflect the current date
        self.update_views(self.date)

    def on_date_change(self, date):
        """Update views when the date is changed."""
        self.update_views(date)

    def update_views(self, date):
        """Refresh the students available and attending for the given date."""
        self.date = date

        # Get correct date format
        self.date_string = date.toString(self.date_format)

        # Get student attendance for the given date
        self.curr_students = self.db.get_attendance_for_date(self.date_string)

        # Clear the items in the list
        self.ui.attendListWidget.clear()
        self.ui.availListWidget.clear()

        # Check to see if a student has a nickname
        # If not, use their first and last name
        for item in self.curr_students:
            if item[1] != None:
                name = str(item[1])
            else:
                name = str(item[2]) + ' ' + str(item[3])
            # Add student to the attended list view
            self.ui.attendListWidget.addItem(name)
        
        # Get all students
        self.students = self.db.get_students()

        # Check to see if a student has a nickname
        # If not, use their first and last name
        for item in self.students:
            # Dont add them to available list if they attended given date
            if item not in self.curr_students:
                if item[1] != None:
                    name = str(item[1])
                else:
                    name = str(item[2]) + ' ' + str(item[3])
                # Add student to available list view
                self.ui.availListWidget.addItem(name)

            # Add student and Sid to student dictionary
            self.student_dict[name] = item[0]

    def on_add_clicked(self):
        """Move student from available to attended list."""
        # Get selected item in list
        ci = self.ui.availListWidget.currentItem()
        # Convert to string
        curr_student =  str(ci.text())
        try:
            # Actually add the student for the date into the database
            self.db.student_attend(self.student_dict[curr_student], \
                    self.date_string)
            self.update_views(self.date)
        except KeyError:
            # Display error window if student missing
            err_msg = QtGui.QErrorMessage()
            err_msg.showMessage("Sid nto found for student %s" % curr_student) 


    def on_remove_clicked(self):
        """Move student from attended to available list."""
        # Get selected item in list
        ci = self.ui.attendListWidget.currentItem()
        # Convert to string
        curr_student =  str(ci.text())
        try:
            # Actually remove the student for the date from the database
            self.db.student_deattend(self.student_dict[curr_student], \
                    self.date_string)
            self.update_views(self.date)
        except KeyError:
            # Display error window if student missing
            err_msg = QtGui.QErrorMessage()
            err_msg.showMessage("Sid nto found for student %s" % curr_student) 
    
def main():
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
