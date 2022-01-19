import csv
import math
import stem_and_leaf_functions as sl
    
def main():
    csvData = sl.getCsvData()

    # print(csvData)
    
    stem = float(input("What is the stem?: "))
    leaf = float(input("What is the leaf?: "))
    
    MAX = float(max(csvData))
    MIN = float(min(csvData))

    stems = []
    [stems.append(sl.firstDigit(n)) for n in csvData]
    stems = list(set(stems)) # ex: 

# [10, 11, 21, 32, 41]
# [1, 2, 3, 4]
# [0,1]
# [1]
# [2]
# [1]
#R: {10: "0, 1", 20: "1", 30: "2", 40: "1"}

    for i in stems:
        print()
        print("{}| ".format(int(i)), end="")
        a = 0
        for data in csvData:
            if(sl.firstDigit(data)*sl.place(stem, 0) == i*stem):
                a+=1
                if(a == 1):
                    print("{}".format(int(data % stem)), end="")
                else:
                    print(", {}".format(int(data % stem)), end="")
            else:
                continue
    print("\nStem:", stem, ",", "Leaf:", leaf)

    
        


main()