from PyQt4 import QtCore, QtGui, Qt

from studentswindow import Ui_studentsDialog
from attendb import AttendDB

class Students(QtGui.QDialog):

    def __init__(self):
        QtGui.QDialog.__init__(self)

        # setup
        self.dialog = Ui_studentsDialog()
        self.dialog.setupUi(self)

        self.sid = None

        header = ['Sid','Apelido', 'First Name', 'Last Name']
        self.dialog.studentTableWidget.setHorizontalHeaderLabels(header)

        self.connect(self.dialog.studentTableWidget, \
                     QtCore.SIGNAL("cellClicked(int, int)"), \
                     self._on_cell_click)
        self.connect(self.dialog.updateButton, QtCore.SIGNAL("clicked()"), \
                    self._on_update_click)

        self.db = AttendDB()

        self._update_list()        

    def _update_list(self):
        """Refresh the student list."""
        #for i in range(self.dialog.studentTableWidget.rowCount()):
        #    self.dialog.studentTableWidget.removeRow(i)
        self.dialog.studentTableWidget.clear()

        rows = self.dialog.studentTableWidget.rowCount()
        students = self.db.get_students()

        while(rows < len(students)):
            self.dialog.studentTableWidget.insertRow(rows)
            rows += 1
    
        for i, student in enumerate(students):
            #self.dialog.studentTableWidget.insertRow(i)
            for j, item in enumerate(student):
                if item == None:
                    item = ''
                newitem = QtGui.QTableWidgetItem(str(item))
                self.dialog.studentTableWidget.setItem(i, j, newitem)
            if self.sid != None and str(student[0]) == str(self.sid):
                self.dialog.studentTableWidget.setCurrentItem(newitem)


        self.dialog.studentTableWidget.sortItems(1)

    def _on_cell_click(self, row, column):
        """Fill out the entries when a cell is clicked."""
        items = self.dialog.studentTableWidget.selectedItems()
        #for item in items:
        #    print item.text()

        # Set the input fields
        self.dialog.nickNameInput.setText(items[1].text())
        self.dialog.firstNameInput.setText(items[2].text())
        self.dialog.lastNameInput.setText(items[3].text())

    def _on_update_click(self):
        """Update current student or add new student."""
        items = self.dialog.studentTableWidget.selectedItems()
        self.sid = str(items[0].text())
        apelido = str(self.dialog.nickNameInput.text())
        fn = str(self.dialog.firstNameInput.text())
        ln = str(self.dialog.lastNameInput.text())

        self.db.update_student(self.sid, apelido, fn, ln)
        
        self._update_list()

    def _on_new_click(self):


        #self.dialog.studentTableWidget.clear()

#class TableModel(QtCore.QAbstractTableModel):

#    def __init__(self, datain, headerdata, parent=None): 
#        """ datain: a list of lists
#            headerdata: a list of strings
#        """
#        QtCore.QAbstractTableModel.__init__(self, parent) 
#        self.arraydata = datain
#        self.headerdata = headerdata
# 
#    def rowCount(self, parent): 
#        return len(self.arraydata) 
# 
#    def columnCount(self, parent): 
#        return len(self.arraydata[0]) 
# 
#    def data(self, index, role): 
#        if not index.isValid(): 
#            return QtCore.QVariant() 
#        elif role != QtCore.Qt.DisplayRole: 
#            return QtCore.QVariant() 
#        return QtCore.QVariant(self.arraydata[index.row()][index.column()]) 

#    def headerData(self, col, orientation, role):
#        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
#            return QtCore.QVariant(self.headerdata[col])
#        return QtCore.QVariant()

#    def sort(self, Ncol, order):
#        """Sort table by given column number.
#        """
#        self.emit(QtCore.SIGNAL("layoutAboutToBeChanged()"))
#        self.arraydata = sorted(self.arraydata, key=operator.itemgetter(Ncol))        
#        if order == QtCore.Qt.DescendingOrder:
#            self.arraydata.reverse()
#        self.emit(QtCore.SIGNAL("layoutChanged()"))
#        
