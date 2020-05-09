import csv
import pandas
import numpy
#This function Adds Header to CSV File
def add_column_names(src, headers = ["Company Name","NAN","Open","High","Low","Close","G","Null","Null"]):
    data = open(src,'r').read()
    with open(src, "w") as fp:
        fp.write(",".join(headers))
        fp.write("\n")
        fp.write(data)
#Above function should only be called once when the CSV file doesn't has header
#This function is used to Read CSV file and take specific values
def csv_reader(x,i):
    data = pandas.read_csv(x)
    y = data.iloc[:,i]
    return y
#This function determines which strikes should be traded
def leg_tracker(x,y,m,n):
    l = 0
    i = 0
    upper_leg = {}
    lower_leg = {}
    Strangle = {
        'Upper Leg' : upper_leg,
        'Lower Leg' : lower_leg
    }
    while l < len(m):
        while i < len(n):
            if x[l] == '09:08' and round(m[l],2) == round(n[i],2):
                a = (m[l+5]//50)*50
                b = a + 50
                atm = int(b if m[l+5] > a + 25 else a)
                upper_leg[y[i]] = atm + 100
                lower_leg[y[i]] = atm - 100
                i += 1
                l += 1
            else :
                l += 1
        break
    return Strangle
