#!/usr/bin/env python3
#lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department

import ipdb

Department.drop_table()
Department.create_table()

payroll = Department.create("Payroll", "Building A, 5th Floor")
print(payroll)  # <Department 1: Payroll, Building A, 5th Floor>

hr = Department.create("Human Resources", "Building C, East Wing")
print(hr)  # <Department 2: Human Resources, Building C, East Wing>

hr.name = 'HR'
hr.location = "Building F, 10th Floor"
hr.update()
print(hr)  # <Department 2: HR, Building F, 10th Floor>

print("Delete Payroll")
payroll.delete()  # delete from db table, object still exists in memory
print(payroll)  # <Department 1: Payroll, Building A, 5th Floor>

ipdb.set_trace()