SELECT Employees.employee_number as "Employee Number", Employees.full_name as "Name", Employees.role as "Job Title", 
Employees.start_date as "Start Date", gross_income as "Gross Income", "net_income" as "Net Income"
FROM Employees 
LEFT JOIN Payslips 
ON Employees.employee_number = Payslips.employee_number