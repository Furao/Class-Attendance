# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'students.ui'
#
# Created: Sun Sep 11 12:53:35 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_studentsDialog(object):
    def setupUi(self, studentsDialog):
        studentsDialog.setObjectName(_fromUtf8("studentsDialog"))
        studentsDialog.resize(512, 622)
        studentsDialog.setWindowTitle(QtGui.QApplication.translate("studentsDialog", "Students", None, QtGui.QApplication.UnicodeUTF8))
        self.layoutWidget = QtGui.QWidget(studentsDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 478, 581))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.studentTableWidget = QtGui.QTableWidget(self.layoutWidget)
        self.studentTableWidget.setEnabled(True)
        self.studentTableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.studentTableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.studentTableWidget.setAlternatingRowColors(True)
        self.studentTableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.studentTableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.studentTableWidget.setColumnCount(4)
        self.studentTableWidget.setObjectName(_fromUtf8("studentTableWidget"))
        self.studentTableWidget.setRowCount(0)
        self.studentTableWidget.horizontalHeader().setVisible(True)
        self.studentTableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.studentTableWidget)
        spacerItem = QtGui.QSpacerItem(474, 38, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.nickNameLabel = QtGui.QLabel(self.layoutWidget)
        self.nickNameLabel.setText(QtGui.QApplication.translate("studentsDialog", "&Apelido:", None, QtGui.QApplication.UnicodeUTF8))
        self.nickNameLabel.setObjectName(_fromUtf8("nickNameLabel"))
        self.gridLayout.addWidget(self.nickNameLabel, 0, 0, 1, 1)
        self.nickNameInput = QtGui.QLineEdit(self.layoutWidget)
        self.nickNameInput.setObjectName(_fromUtf8("nickNameInput"))
        self.gridLayout.addWidget(self.nickNameInput, 0, 1, 1, 1)
        self.activeCheckBox = QtGui.QCheckBox(self.layoutWidget)
        self.activeCheckBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.activeCheckBox.setText(QtGui.QApplication.translate("studentsDialog", "Active?", None, QtGui.QApplication.UnicodeUTF8))
        self.activeCheckBox.setObjectName(_fromUtf8("activeCheckBox"))
        self.gridLayout.addWidget(self.activeCheckBox, 0, 2, 1, 2)
        self.firstNameLabel = QtGui.QLabel(self.layoutWidget)
        self.firstNameLabel.setText(QtGui.QApplication.translate("studentsDialog", "&First Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.firstNameLabel.setObjectName(_fromUtf8("firstNameLabel"))
        self.gridLayout.addWidget(self.firstNameLabel, 1, 0, 1, 1)
        self.firstNameInput = QtGui.QLineEdit(self.layoutWidget)
        self.firstNameInput.setObjectName(_fromUtf8("firstNameInput"))
        self.gridLayout.addWidget(self.firstNameInput, 1, 1, 1, 1)
        self.lastNameLabel = QtGui.QLabel(self.layoutWidget)
        self.lastNameLabel.setText(QtGui.QApplication.translate("studentsDialog", "&Last Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lastNameLabel.setObjectName(_fromUtf8("lastNameLabel"))
        self.gridLayout.addWidget(self.lastNameLabel, 1, 2, 1, 1)
        self.lastNameInput = QtGui.QLineEdit(self.layoutWidget)
        self.lastNameInput.setObjectName(_fromUtf8("lastNameInput"))
        self.gridLayout.addWidget(self.lastNameInput, 1, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem1 = QtGui.QSpacerItem(474, 48, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.newButton = QtGui.QPushButton(self.layoutWidget)
        self.newButton.setText(QtGui.QApplication.translate("studentsDialog", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.newButton.setObjectName(_fromUtf8("newButton"))
        self.horizontalLayout.addWidget(self.newButton)
        self.updateButton = QtGui.QPushButton(self.layoutWidget)
        self.updateButton.setText(QtGui.QApplication.translate("studentsDialog", "&Update/Add", None, QtGui.QApplication.UnicodeUTF8))
        self.updateButton.setObjectName(_fromUtf8("updateButton"))
        self.horizontalLayout.addWidget(self.updateButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.buttonBox = QtGui.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.nickNameLabel.setBuddy(self.nickNameInput)
        self.firstNameLabel.setBuddy(self.firstNameInput)
        self.lastNameLabel.setBuddy(self.lastNameInput)

        self.retranslateUi(studentsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), studentsDialog.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), studentsDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(studentsDialog)
        studentsDialog.setTabOrder(self.nickNameInput, self.activeCheckBox)
        studentsDialog.setTabOrder(self.activeCheckBox, self.firstNameInput)
        studentsDialog.setTabOrder(self.firstNameInput, self.lastNameInput)
        studentsDialog.setTabOrder(self.lastNameInput, self.newButton)

    def retranslateUi(self, studentsDialog):
        pass

