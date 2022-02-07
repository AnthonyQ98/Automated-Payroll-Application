from pushToDB import *

print("*" * 50)
print("\t\t\t\tPAYROLL SYSTEM")
print("*" * 50)

# RECEIVE EMPLOYEE DATA
employee_name = input("\t\t\t\tEmployee Name: \n")
employee_number = int(input("\t\t\t\tEmployee Number: \n"))
total_income = float(input("\t\t\t\tYearly Income: \n"))
pension_percent = int(input("Pension % (type '0' if no pension): \n"))
self_employed_binary = input("Self Employed (y/n): \n")

# CONSTANTS
EMPLOYEE_TAX_ALLOWANCE = 1700
LOWER_TAX_BAND = .20
HIGHER_TAX_BAND = .40
GROSS_MONTHLY_INCOME = total_income / 12
LOWER_USC = .005
MID_USC = .02
HIGH_USC = .045
HIGHER_USC = .08
HIGHEST_USC = 0.11
LOWER_HIGH_TAX_THRESHOLD = 36800
MONTHS_PER_YEAR = 12
USC_CUTOFF = 13000
DECIMAL_PLACES_ROUND = 2



def calculate_usc():
    usc_deductible = 0
    if total_income >= 100000 and self_employed_binary == "y":
        usc_deductible = ((total_income - 100000) * HIGHEST_USC) + ((100000 - 70044) * 0.08) + ((70044 - 21295) * 0.045) + ((21295 - 12012) * 0.02) + (12012 * 0.005)
    elif total_income >= 70044.01:
        usc_deductible = ((total_income - 70044) * 0.08) + ((70044 - 21295) * 0.045) + ((21295 - 12012) * 0.02) + (12012 * 0.005)
    elif total_income >= 21295.01 and total_income < 70044:
        usc_deductible = ((total_income - 21295) * 0.045) + ((21295 - 12012) * 0.02) + (12012 * 0.005)
    elif total_income >= 12012.01 and total_income < 21295:
        usc_deductible = ((total_income - 12012) * 0.02) + (12012 * 0.005)
    else:
        usc_deductible = (total_income * 0.005)
    return usc_deductible

# GROSS INCOME BEFORE ANY DEDUCTIONS:
print(f"Gross Monthly Income: {round(GROSS_MONTHLY_INCOME, DECIMAL_PLACES_ROUND)}")

pension_contributions = 0

# PENSION CALCULATIONS:
if pension_percent > 0:
    pension_contributions = (total_income / 100 * pension_percent) / MONTHS_PER_YEAR
    print(f"Pension Contributions: €{round(pension_contributions, DECIMAL_PLACES_ROUND)}")
else:
    pension_contributions = 0

print(f"Tax Allowance (annually): €{EMPLOYEE_TAX_ALLOWANCE}")
print(f"Tax Allowance (monthly): €{round(EMPLOYEE_TAX_ALLOWANCE / MONTHS_PER_YEAR, DECIMAL_PLACES_ROUND)}")

# LOWER TAX BAND CALCULATIONS:
if total_income <= LOWER_HIGH_TAX_THRESHOLD:
    deductible_tax = total_income * LOWER_TAX_BAND - EMPLOYEE_TAX_ALLOWANCE
    print(f"PAYE Tax (incl. allowance): €{round(deductible_tax / MONTHS_PER_YEAR, DECIMAL_PLACES_ROUND)}")
    net_income = total_income - deductible_tax
    net_income = net_income / MONTHS_PER_YEAR
    usc_monthly = round(calculate_usc() / MONTHS_PER_YEAR, DECIMAL_PLACES_ROUND)
    print(f"USC Monthly: €{usc_monthly}")
    net_income = net_income - usc_monthly - pension_contributions
    print(f"Net Monthly Income: €{round(net_income, DECIMAL_PLACES_ROUND)}")

# HIGHER TAX BAND CALCULATIONS:
elif total_income > LOWER_HIGH_TAX_THRESHOLD:
    deductible_tax = ((total_income - LOWER_HIGH_TAX_THRESHOLD) * HIGHER_TAX_BAND) + (LOWER_HIGH_TAX_THRESHOLD * LOWER_TAX_BAND) - EMPLOYEE_TAX_ALLOWANCE
    print(f"PAYE Tax (incl. allowance): €{round(deductible_tax / MONTHS_PER_YEAR, DECIMAL_PLACES_ROUND)}")
    net_income = total_income - deductible_tax
    net_income = net_income / MONTHS_PER_YEAR
    if total_income > USC_CUTOFF:
        usc_monthly = round(calculate_usc() / MONTHS_PER_YEAR, DECIMAL_PLACES_ROUND)
        print(f"USC Monthly: €{usc_monthly}")
        net_income = net_income - usc_monthly - pension_contributions
    print(f"Net Monthly Income: €{round(net_income, DECIMAL_PLACES_ROUND)}")

new_record_to_db(employee_name, employee_number, total_income, deductible_tax, pension_percent, round(net_income, 2), usc_monthly, round(pension_contributions, 2), self_employed_binary, round(EMPLOYEE_TAX_ALLOWANCE / 12, 2))

fetch_records(employee_number)



