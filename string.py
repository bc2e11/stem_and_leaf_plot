import random
import csv


header = ['string', 'number']

rows = []
nums = []
with open("numbers.csv", mode="w") as f:
    csvw = csv.writer(f)
    csvw.writerow(header)
    
    for i in range(1,100):
        k = random.randint(1,100)
        csvw.writerow([k])
# f = open("numbers.csv", "r")
# 
# nums = f.readlines()
# 
# Nums = [int(num[0]) for num in nums]
# 
# print(Nums)
# 




