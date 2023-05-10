print("Multiplication table from 1 to 10")
MultiTable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for x in MultiTable:
    for i in range(1, 11):
        print(x * i, end=" ")
    print("\t")
    
input("Exit")
