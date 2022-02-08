# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\employee_viewallpayroll_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EmployeePayrollWindow(object):

    def setupUi(self, EmployeePayrollWindow):
        EmployeePayrollWindow.setObjectName("EmployeePayrollWindow")
        EmployeePayrollWindow.resize(1009, 570)
        self.employeeNameLbl = QtWidgets.QLabel(EmployeePayrollWindow)
        self.employeeNameLbl.setGeometry(QtCore.QRect(110, 90, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.employeeNameLbl.setFont(font)
        self.employeeNameLbl.setObjectName("employeeNameLbl")
        self.warningLoggedInMsg = QtWidgets.QLabel(EmployeePayrollWindow)
        self.warningLoggedInMsg.setGeometry(QtCore.QRect(220, 370, 611, 41))
        self.warningLoggedInMsg.setObjectName("warningLoggedInMsg")
        self.employeeNumLbl = QtWidgets.QLabel(EmployeePayrollWindow)
        self.employeeNumLbl.setGeometry(QtCore.QRect(510, 90, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.employeeNumLbl.setFont(font)
        self.employeeNumLbl.setObjectName("employeeNumLbl")
        self.dateLbl = QtWidgets.QLabel(EmployeePayrollWindow)
        self.dateLbl.setGeometry(QtCore.QRect(110, 20, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dateLbl.setFont(font)
        self.dateLbl.setObjectName("dateLbl")
        self.displayPayrollTable = QtWidgets.QTableWidget(EmployeePayrollWindow)
        self.displayPayrollTable.setGeometry(QtCore.QRect(120, 180, 741, 181))
        self.displayPayrollTable.setLineWidth(1)
        self.displayPayrollTable.setRowCount(3)
        self.displayPayrollTable.setColumnCount(6)
        self.displayPayrollTable.setObjectName("displayPayrollTable")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.displayPayrollTable.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.displayPayrollTable.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.displayPayrollTable.setItem(2, 5, item)
        self.displayPayrollTable.horizontalHeader().setDefaultSectionSize(120)
        self.displayPayrollTable.verticalHeader().setDefaultSectionSize(50)

        self.retranslateUi(EmployeePayrollWindow)
        QtCore.QMetaObject.connectSlotsByName(EmployeePayrollWindow)

    def retranslateUi(self, EmployeePayrollWindow):
        _translate = QtCore.QCoreApplication.translate
        EmployeePayrollWindow.setWindowTitle(_translate("EmployeePayrollWindow", "View Payroll"))
        self.employeeNameLbl.setText(_translate("EmployeePayrollWindow", "Employee Name: "))
        self.warningLoggedInMsg.setText(_translate("EmployeePayrollWindow", "PLEASE NOTE: As you are logged in as an employee and not admin, you can only view your own payroll information"))
        self.employeeNumLbl.setText(_translate("EmployeePayrollWindow", "Employee Number:"))
        self.dateLbl.setText(_translate("EmployeePayrollWindow", "Date:"))
        __sortingEnabled = self.displayPayrollTable.isSortingEnabled()
        self.displayPayrollTable.setSortingEnabled(False)
        item = self.displayPayrollTable.item(0, 5)
        item.setText(_translate("EmployeePayrollWindow", "PDF"))
        item.setForeground(QtGui.QBrush(QtGui.QColor(0, 255, 0)))
        item = self.displayPayrollTable.item(1, 5)
        item.setText(_translate("EmployeePayrollWindow", "PDF"))
        item.setForeground(QtGui.QBrush(QtGui.QColor(0, 255, 0)))
        item = self.displayPayrollTable.item(2, 5)
        item.setText(_translate("EmployeePayrollWindow", "PDF"))
        item.setForeground(QtGui.QBrush(QtGui.QColor(0, 255, 0)))
        self.displayPayrollTable.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EmployeePayrollWindow = QtWidgets.QWidget()
    ui = Ui_EmployeePayrollWindow()
    ui.setupUi(EmployeePayrollWindow)
    EmployeePayrollWindow.show()
    sys.exit(app.exec_())
