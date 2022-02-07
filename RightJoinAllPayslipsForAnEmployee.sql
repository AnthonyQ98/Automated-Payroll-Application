SELECT Payslips.*, Employees.full_name
FROM Payslips
LEFT JOIN Employees
ON Payslips.employee_number = Employees.employee_number
WHERE Payslips.employee_number = 111