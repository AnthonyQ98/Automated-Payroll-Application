import sqlite3
import sys

"""
grossIncome = total_income
deductibleTax = deductible_tax
pensionContributions = pension_contributions
uscMonthly = usc_monthly
netIncome = net_income

print("Net income: ", netIncome)
"""




def connect_to_db():
    try:
        database_file = "data.db"
        connection = sqlite3.connect(database_file)
        print("DB STATUS: Successful connection to the database!")
        crsr = connection.cursor()
        return {connection, crsr}
    except Exception as e:
        print(f"ERROR: ", e)


def new_record_to_db(employee_number, total_income, hours_worked, deductible_tax, pension_percent,
                     net_income, usc_monthly, pension_contributions, self_employed_binary, EMPLOYEE_TAX_ALLOWANCE):
    (crsr, connection) = connect_to_db()
    crsr = connection.cursor()
    print("Here cursor")
    try:
        sql_command = f"""INSERT INTO Payslips (employee_number, gross_income, hours_worked, pension_percent, pension_contributions, self_employed, income_tax, usc, tax_allowance, net_income, date_created) VALUES ({employee_number}, {total_income}, {hours_worked}, {pension_percent}, {pension_contributions}, "{self_employed_binary}", {deductible_tax}, {usc_monthly}, {EMPLOYEE_TAX_ALLOWANCE}, {net_income}, CURRENT_TIMESTAMP);"""
        crsr.execute(sql_command)
    except Exception as e:
        print(e)
    print("TEST")
    connection.commit()
    print("DB STATUS: Successfully added new payment info in to the database!")
    connection.close()
    print("DB STATUS: Closed the connection.")

def fetch_records(employee_number):
    (crsr, connection) = connect_to_db()
    crsr = connection.cursor()
    crsr.execute(f"""SELECT Payslips.*, Employees.full_name
FROM Payslips
LEFT JOIN Employees
ON Payslips.employee_number = Employees.employee_number
WHERE Payslips.employee_number = {employee_number};""")
    fetched_records_list = crsr.fetchall()
    for i in fetched_records_list:
        print(i)
    print(f"DB STATUS: {len(fetched_records_list)} matched records have been found!")
    connection.close()
    print("DB STATUS: Closed the connection.")

def fetch_hourly_rate(employee_number):
    print("Inside pushtodb.py:", type(employee_number))
    (crsr, connection) = connect_to_db()
    crsr = connection.cursor()
    crsr.execute(f"""SELECT Employees.hourly_rate FROM Employees WHERE Employees.employee_number = {employee_number};""")
    result = crsr.fetchone()
    print("Results: ", result)
    print(f"DB STATUS: Hourly rate has been found!")
    connection.close()
    print("DB STATUS: Closed the connection.")
    return result

def check_user_log_in(employeeNumber, pinNumber):
    (crsr, connection) = connect_to_db()
    crsr = connection.cursor()
    print("DB STATUS: Checking log in credentials in the database!")
    crsr.execute(f"""SELECT employee_number, pin FROM Employees WHERE employee_number = "{employeeNumber}" AND pin = "{pinNumber}";""")
    result = crsr.fetchall()
    for i in result:
        print(i)
    print(f"DB STATUS: Matched records have been found! Signing in...")
    connection.close()
    print("DB STATUS: Closed the connection.")
    return result

def fetch_user_last_three_payroll_from_db(employeeNumber):
    (crsr, connection) = connect_to_db()
    crsr = connection.cursor()
    print("DB STATUS: Fetching logged in users details and payroll information from the database.!")
    crsr.execute(f"""SELECT * FROM Employees LEFT JOIN Payslips ON Employees.employee_number = Payslips.employee_number WHERE Employees.employee_number = {employeeNumber} ORDER BY Payslips.date_created DESC LIMIT 3;""")
    result = crsr.fetchall()
    print(result)
    print(f"DB STATUS: Loading employee records...")
    connection.close()
    print("DB STATUS: Finished - Closed the connection.")
    return result


