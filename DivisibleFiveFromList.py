givenList = [12, 20, 30, 86, 35]

print("Display numbers divisible by 5 from a list \n")
print("Given list is: ", givenList)
print("Divisible by 5: ")

#check every item in list whether it can be divided by five
for i in givenList:
        if i % 5 == 0:
            print(i)

input("Exit")