#! /usr/bin/env python3
import sys
if __name__ == '__main__':
    try:     
        wages = int(sys.argv[1])
        ysd = wages - 3500
        tax = 0
        if 0 < ysd <= 1500:
            tax = ysd * 0.03
        elif 1500 < ysd <= 4500:
            tax = ysd * 0.1 - 105
        elif 4500 < ysd <= 9000:
            tax = ysd * 0.2 - 555
        elif 9000 < ysd <= 35000:
            tax = ysd * 0.25 - 1005
        elif 35000 < ysd <= 55000:
            tax = ysd * 0.30 - 2755
        elif 55000 < ysd <= 80000:
            tax = ysd * 0.35 - 5505
        elif tax > 80000:
            tax = ysd * 0.45 - 13505
        else:
            tax  = 0 
        print(format(tax,".2f"))
    except Exception as ex:
        print("Parameter Error")     

      
