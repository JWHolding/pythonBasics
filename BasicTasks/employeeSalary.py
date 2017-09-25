#!/usr/bin/python

employee = "Jacob"
salary = 700000
tax = salary*21/100
net_salary = salary - tax
print("Employee:", employee)
print("Salary: £%0.2f" % salary)
print("Tax: £%0.2f" % tax)
print("Net Pay = £%0.2f" % net_salary)
