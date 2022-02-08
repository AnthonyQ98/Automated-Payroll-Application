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

class LoginWindow(QtWidgets.QMainWindow, log_in_window):
    logged = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.btn_logIn.clicked.connect(self.authenticate)

    @QtCore.pyqtSlot()
    def authenticate(self):
        db_user = self.employeeNumInput.text()
        db_pass = self.employeePinInput.text()

        result = LoginWindow.login(self, emp_number=db_user, pin_number=db_pass)
        print(f"TESTING RESULT: {result}")
        if result[0][0] == 'admin' and result[0][1] == 'admin':
            print("Logged in as ADMIN.")
            self.logged.emit()
            self.close()
        elif result == "None":
            print("No results found!")

        else:
            print("Logged in as EMPLOYEE.")
        """
                else:
            result = LoginWindow.login(self, emp_number=db_user, pin_number=db_pass)
            print("Result here", result)
            if result == 1:
                print(f"Logged in as EMPLOYEE!")
                self.logged.emit()
                self.close()
            elif result == 2:
                print(f"Logged in as ADMIN!")
                self.logged.emit()
                self.close()
            else:
                print("Invalid credentials.")
                isClicked = "NO"
            return result
        """

        return result

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    windowlogin = LoginWindow()
    w = Main_Window()
    pwind = Payroll_Window()
    windowlogin.show()
    windowlogin.logged.connect(w.show)
    print(f"TESTING DOWN HERE: ", windowlogin.result[0][0])
    windowlogin.logged.connect(pwind.show)

    sys.exit(app.exec_())


if __name__ == '__main__': main()