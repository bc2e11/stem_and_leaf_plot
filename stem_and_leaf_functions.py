import math

def firstDigit(k): # returns the first digit of any number k given
    d = int(math.log10(k))
    d = int(k/pow(10,d))
    return d
    
def place(number, digit):  # returns the place in decimal system a value represents (ex: 0 in 231012 represents the hundreds place)
    n1 = (int)(number/firstDigit(number))
    place = (n1 - (n1 % (10**(len(str(n1))-1))))/(10 ** digit) 
    return place

def branch(number):
    branch = firstDigit(number) * place(number, len(str(firstDigit(number)))-1)
    return branch

def getCsvData():
    import csv
    csvData = []
    path = "/Users/bhagawatchapagain/Desktop/dev/py/stem and leaf plot maker/numbers.csv"
    f = open(path, "r")
    csv = csv.reader(f)
    
    for row in csv:
        csvData.append(row[0])
    
    csvData.__delitem__(0)
    
    csvData = sorted([float(number) for number in csvData])

    return csvData
