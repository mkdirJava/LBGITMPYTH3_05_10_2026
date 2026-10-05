from collections import namedtuple
fields = ["field1", "field2"]
Subclass = namedtuple("Subclass", fields)
Employee = namedtuple("Employee",["name", "age", "phone"],defaults=["Anon", 0, None])
var = Subclass(field1="FIELD1", field2="FIELD2")
var2 = Employee(name="Ted", age=23, phone="01273700955")
print(f"{var.field1}, {var.field2}")
print(f"{var2.name}, {var2.age}, {var2.phone}")

Employee = namedtuple("Employee",["name", "age", "phone"], defaults=["Anon", 0, None])
emp = Employee(name="Ted", age=23, phone="01273700955")
emp2 = Employee()
print(f"{emp.name}, {emp.age}, {emp.phone}")
print(f"{emp2.name}, {emp2.age}, {emp2.phone}")


from collections import namedtuple

EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')

import csv
for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rt"))):
    print(emp.name, emp.title)

import sqlite3
conn = sqlite3.connect('companydata.db')
cursor = conn.cursor()
cursor.execute('SELECT name, age, title, department, paygrade FROM employees')
for emp in map(EmployeeRecord._make, cursor.fetchall()):
    print(emp.name, emp.title)

