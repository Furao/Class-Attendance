import os
import sys

from PyQt4 import QtCore, QtGui
from mainwindow import Ui_MainWindow
from attendb import AttendDB
from students import Students

class Main(QtGui.QMainWindow):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        # Setup the main window
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        # Set date to today
        self.date = QtCore.QDate.currentDate()
        self.ui.calendarWidget.setSelectedDate(self.date)

        # Date format for SQLite
        self.date_format = "yyyy-MM-dd"

        # Used to remember the Students Id
        self.student_dict = {}
        
        # Create Attendance DB Connection Object
        self.db = AttendDB()

        # Create list models
        self.availModel = QtGui.QStandardItemModel(0, 2)
        self.attendModel = QtGui.QStandardItemModel(0, 2)

        self.ui.availListView.setModel(self.availModel)
        self.ui.attendListView.setModel(self.attendModel)

        # Connect signals to handlers
        self.connect(self.ui.addButton, QtCore.SIGNAL("clicked()"), \
                self.on_add_clicked)
        self.connect(self.ui.removeButton, QtCore.SIGNAL("clicked()"), \
                self.on_remove_clicked)
        self.connect(self.ui.calendarWidget, \
                QtCore.SIGNAL("selectionChanged()"), \
                self.on_date_change)

        self.connect(self.ui.actionEdit_Students, \
                QtCore.SIGNAL("triggered()"), \
                self.on_edit_students_select)
        # Update the lists to reflect the current date
        self.update_views()

    def on_edit_students_select(self):
        """Open the editing student window."""
        edit_window = Students()
        edit_window.exec_()

    def on_date_change(self):
        """Update views when the date is changed."""
        self.date = self.ui.calendarWidget.selectedDate()
        self.update_views()

    def update_views(self):
        """Refresh the students available and attending for the given date."""
        # Get correct date format
        self.date_string = self.date.toString(self.date_format)
        
        # Clear Models
        self.availModel.clear()
        self.attendModel.clear()
        
        for student in self.db.get_attendance_for_date(self.date_string):
            if student[1] != None and student[1] != '':
                name = str(student[1])
            else:
                name = str(student[2]) + ' ' + str(student[3])
            # Add student to the attended list view
            itemlist = [QtGui.QStandardItem(name), \
                    QtGui.QStandardItem(str(student[0]))]
            self.attendModel.appendRow(itemlist)


        for student in self.db.get_students():
            # Don't add them to available list if they attended given date
            if student[1] != None and student[1] != '':
                name = str(student[1])
            else:
                name = str(student[2]) + ' ' + str(student[3])
            # Add student to available list view
            itemlist = [QtGui.QStandardItem(name), \
                    QtGui.QStandardItem(str(student[0]))]
            if self.attendModel.findItems(name) == []:
                self.availModel.appendRow(itemlist)


        self.availModel.sort(0)
        self.attendModel.sort(0)

    
    def on_add_clicked(self):
        """Move student from available to attended list."""
        selected_indexes = self.ui.availListView.selectedIndexes()
        for index in selected_indexes:
            row = self.availModel.itemFromIndex(index).row()
            #rowList = self.availModel.takeRow(row)
            student = self.availModel.item(row, 0).text()
            sid = self.availModel.item(row, 1).text()
            try:
                # Actually add the student for the date into the database
                self.db.student_attend(sid, self.date_string)
            except KeyError:
                # Display error window if student missing
                err_msg = QtGui.QErrorMessage()
                err_msg.showMessage("Sid not found for student %s" % student)

        self.update_views()
        


    def on_remove_clicked(self):
        """Move student from attended to available list."""
        selected_indexes = self.ui.attendListView.selectedIndexes()
        for index in selected_indexes:
            row = self.attendModel.itemFromIndex(index).row()
            student = self.attendModel.item(row, 0).text()
            sid = self.attendModel.item(row, 1).text()
            try:
                # Actually add the student for the date into the database
                self.db.student_deattend(sid, self.date_string)
            except KeyError:
                # Display error window if student missing
                err_msg = QtGui.QErrorMessage()
                err_msg.showMessage("Sid not found for student %s" % student)

        self.update_views()
    
def main():
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    window.raise_()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
