import csv

f = open("stem and leaf plots.csv", "r")
csv = csv.reader(f)

numbers = []

for row in csv:
    numbers.append(row[1])

numbers.__delitem__(0)

numbers = sorted([float(number) for number in numbers])

stem = input("What is your stem? ")
leaf = input("What is your leaf? ")

