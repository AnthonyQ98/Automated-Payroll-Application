# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'application_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from tax_calculations import calculate_tax
from pushToDB import new_record_to_db, fetch_hourly_rate
import datetime
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(881, 597)
        MainWindow.setAutoFillBackground(True)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.main_submitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.main_submitBtn.setGeometry(QtCore.QRect(280, 410, 261, 61))


        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)


        self.main_submitBtn.setFont(font)
        self.main_submitBtn.setObjectName("main_submitBtn")


        self.main_grossIncomeBox = QtWidgets.QLineEdit(self.centralwidget)
        self.main_grossIncomeBox.setGeometry(QtCore.QRect(280, 210, 261, 41))
        self.main_grossIncomeBox.setText("")
        self.main_grossIncomeBox.setObjectName("main_grossIncomeBox")


        # self.main_employeeNameBox = QtWidgets.QLineEdit(self.centralwidget)
        # self.main_employeeNameBox.setGeometry(QtCore.QRect(280, 90, 261, 41))
        # self.main_employeeNameBox.setText("")
        # self.main_employeeNameBox.setObjectName("main_employeeNameBox")
        self.main_employeeNumBox = QtWidgets.QLineEdit(self.centralwidget)
        self.main_employeeNumBox.setGeometry(QtCore.QRect(280, 150, 261, 41))
        self.main_employeeNumBox.setText("")
        self.main_employeeNumBox.setObjectName("main_employeeNumBox")


        self.main_pensionPercentSelector = QtWidgets.QSpinBox(self.centralwidget)
        self.main_pensionPercentSelector.setGeometry(QtCore.QRect(280, 310, 71, 22))
        self.main_pensionPercentSelector.setMaximum(10)
        self.main_pensionPercentSelector.setObjectName("main_pensionPercentSelector")


        self.main_pensionContriLbl = QtWidgets.QLabel(self.centralwidget)
        self.main_pensionContriLbl.setGeometry(QtCore.QRect(80, 295, 191, 51))



        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)


        self.main_pensionContriLbl.setFont(font)
        self.main_pensionContriLbl.setObjectName("main_pensionContriLbl")
        self.main_grossIncomeLbl = QtWidgets.QLabel(self.centralwidget)
        self.main_grossIncomeLbl.setGeometry(QtCore.QRect(100, 220, 200, 19))


        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)


        self.main_grossIncomeLbl.setFont(font)
        self.main_grossIncomeLbl.setObjectName("main_grossIncomeLbl")
        self.main_employeeNumLbl = QtWidgets.QLabel(self.centralwidget)
        self.main_employeeNumLbl.setGeometry(QtCore.QRect(110, 145, 191, 51))


        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)


        self.main_employeeNumLbl.setFont(font)
        self.main_employeeNumLbl.setObjectName("main_employeeNumLbl")
        self.main_nameLbl = QtWidgets.QLabel(self.centralwidget)
        self.main_nameLbl.setGeometry(QtCore.QRect(130, 85, 191, 51))


        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)


        self.main_nameLbl.setFont(font)
        self.main_nameLbl.setObjectName("main_nameLbl")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 881, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.main_submitBtn.clicked.connect(self.update_the_database)

    def update_the_database(self):
        if self.main_grossIncomeBox.text() != "" and self.main_pensionPercentSelector.text() != "" \
                 and self.main_employeeNumBox.text() != "":
            employee_number = int(self.main_employeeNumBox.text())
            print("Employee Number: ", employee_number)
            hourly_rate = fetch_hourly_rate(employee_number)
            print("Hourly Rate: ", hourly_rate[0])
            hours_worked = int(self.main_grossIncomeBox.text())
            print("Hours Worked: ", hours_worked)
            total_income = int(self.main_grossIncomeBox.text()) * hourly_rate[0]
            employee_number = int(self.main_employeeNumBox.text())
            #employee_name = self.main_employeeNameBox.text()
            pension_percent = int(self.main_pensionPercentSelector.text())
            deductible_tax, net_income, usc_monthly, pension_contributions, EMPLOYEE_TAX_ALLOWANCE = calculate_tax(total_income, pension_percent, self_employed_binary="n")
            # Adjust hard coded name and employee number.
            new_record_to_db(employee_number, round(total_income, 2), hours_worked, deductible_tax, pension_percent,
                             round(net_income, 2), usc_monthly, round(pension_contributions, 2), "n",
                             round(EMPLOYEE_TAX_ALLOWANCE / 12, 2))
            self.main_grossIncomeBox.setText("")
            self.main_pensionPercentSelector.setValue(0)
        else:
            print("NEED TO FILL IN THE BOXES.")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AQ Payroll System"))
        self.main_submitBtn.setText(_translate("MainWindow", "SUBMIT"))
        self.main_grossIncomeBox.setPlaceholderText(_translate("MainWindow", "Enter employees hours worked this month!"))
        #self.main_employeeNameBox.setPlaceholderText(_translate("MainWindow", "Employee Name"))
        self.main_employeeNumBox.setPlaceholderText(_translate("MainWindow", "Employee Number"))
        self.main_pensionContriLbl.setText(_translate("MainWindow", "Pension Contributions:"))
        self.main_grossIncomeLbl.setText(_translate("MainWindow", "This Months Hours:"))
        self.main_employeeNumLbl.setText(_translate("MainWindow", "Employee Number:"))
        #self.main_nameLbl.setText(_translate("MainWindow", "Employee Name:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionSave.setText(_translate("MainWindow", "View "))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
