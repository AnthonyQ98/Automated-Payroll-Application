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




try:
    database_file = "insert_here"
    connection = sqlite3.connect(database_file)
    crsr = connection.cursor()
except Exception as e:
    print(f"ERROR: ", e)


def new_record_to_db(employee_name, employee_number, total_income, deductible_tax,
                     net_income, usc_monthly, pension_contributions, EMPLOYEE_TAX_ALLOWANCE):

    print("Test if this function was called: ", employee_number)
    sql_command = f"""INSERT INTO randomTable VALUES ({employee_number}, {employee_name}, {total_income}, {deductible_tax}, {net_income}
    {usc_monthly}, {pension_contributions}, {EMPLOYEE_TAX_ALLOWANCE});"""
    crsr.execute(sql_command)
    connection.commit()
    connection.close()

def fetch_records():
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM randomTable")
    fetched_records_list = crsr.fetchall()
    for i in fetched_records_list:
        print(i)
    connection.close()

# close the connection
connection.close()

