#! /usr/bin/env python3
import sys
def calculator(employee, salary):
    tax = salary * 0.825 - 3500
    ysd = 0
    if tax <= 0:
        result = 0
    elif 0 < tax <= 1500:
        result = tax * 0.03
    elif 1500 < tax <= 4500:
        result = tax * 0.1 - 105
    elif 4500 < tax <= 9000:
        result = tax * 0.2 - 555
    elif 9000 < tax <= 35000:
        result = tax * 0.25 - 1005
    elif 35000 < tax <= 55000:
        result = tax * 0.3 - 2755
    elif 55000 < tax <= 80000:
        result = tax * 0.35 - 5505
    else:
        result = tax * 0.45 - 13505
    ysd = salary * 0.825 - result
    print(str(employee) + ":" + format(ysd, ".2f"))
try:
    for arg in sys.argv[1:]:
        employee = int(arg.split(':')[0])
        salary = int(arg.split(':')[1])
        calculator(employee, salary)
except:
    print("Parameter Error")    
