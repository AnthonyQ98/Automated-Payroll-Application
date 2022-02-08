from login_gui import Ui_MainWindow as log_in_window
from gui import Ui_MainWindow as home_page_window
from viewpayroll_employee_gui import Ui_EmployeePayrollWindow as payroll_window
from PyQt5 import QtCore, QtGui, QtWidgets



class Main_Window(QtWidgets.QMainWindow, home_page_window):
    def __init__(self, parent=None):
        super(Main_Window, self).__init__(parent)
        self.setupUi(self)

class Payroll_Window(QtWidgets.QMainWindow, payroll_window):
    def __init__(self, parent=None):
        super(Payroll_Window, self).__init__(parent)
        self.setupUi(self)

    def openWindow(self):
        self.window = QtWidgets.QWidget()
        self.ui = payroll_window()
        self.ui.setupUi(self.window)
        self.window.show()

class LoginWindow(QtWidgets.QMainWindow, log_in_window):
    logged = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.btn_logIn.clicked.connect(self.openAllPayroll)
       # self.btn_logIn.clicked.connect(self.openAllPayroll)

        #if self.employeeNumInput.text() == "admin" and self.employeePinInput.text() == "admin":
            #self.btn_logIn.clicked.connect(self.openAllPayroll)

    def fetchResult(self, db_user, db_pass):
        return LoginWindow.login(self, emp_number=db_user, pin_number=db_pass)

    def openAllPayroll(self):
        result = self.login(emp_number=self.employeeNumInput.text(), pin_number=self.employeePinInput.text())
        print(result)
        if result[0][0] == "admin" and result[0][1] == "admin":
            #self.btn_logIn.clicked.connect(self.openAdminMenu)
            self.openAdminMenu(result[0][0])
        else:
            print("THIS BLOCK")

            payrollView = Payroll_Window(self)
            payrollView.show()

    def openAdminMenu(self, employeeNumInput):
        employee_number = employeeNumInput
        print(employee_number)
        adminView = Main_Window(self)
        adminView.show()

    @QtCore.pyqtSlot()
    def authenticate(self):
        pass
        #db_user = self.employeeNumInput.text()
        #db_pass = self.employeePinInput.text()

        #result = LoginWindow.login(self, emp_number=db_user, pin_number=db_pass)
        #print(f"TESTING RESULT: {result}")
        #if result[0][0] == 'admin' and result[0][1] == 'admin':
           # print("Logged in as ADMIN.")
            #self.logged.emit()
            #self.close()
        #elif result == "None":
            #print("No results found!")

        #else:
           # print("Logged in as EMPLOYEE.")

            #self.logged.emit()
            #self.close()
        #return result

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    windowlogin = LoginWindow()
    w = Main_Window()
    pwind = Payroll_Window()
    #windowlogin.logged.connect(w.show)
    #windowlogin.logged.connect(pwind.show)
    #windowlogin.logged.emit()
    print("OPENED")
    windowlogin.show()

    sys.exit(app.exec_())


if __name__ == '__main__': main()