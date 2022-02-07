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
        return {crsr, connection}
    except Exception as e:
        print(f"ERROR: ", e)


def new_record_to_db(employee_name, employee_number, total_income, deductible_tax, pension_percent,
                     net_income, usc_monthly, pension_contributions, self_employed_binary, EMPLOYEE_TAX_ALLOWANCE):
    (crsr, connection) = connect_to_db()
    sql_command = f"""INSERT INTO Payslips (full_name, employee_number, gross_income, pension_percent, pension_contributions, self_employed,
     income_tax, usc, tax_allowance, net_income) VALUES ("{employee_name}", {employee_number}, {total_income}, {pension_percent}, 
    {pension_contributions}, "{self_employed_binary}", {deductible_tax}, {usc_monthly}, {EMPLOYEE_TAX_ALLOWANCE}, {net_income});"""
    crsr.execute(sql_command)
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


