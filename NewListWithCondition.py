list1 = [21, 30, 56, 60, 79]
list2 = [10, 34, 39, 55, 91]
newList = []

print("Create a new list from a two list with condition")
print("Fist list only odd numbers:",list1)
print("Second list only even numbers:", list2)

#pick only odd numbers
for i in list1:
    if i % 2 != 0:
        newList.append(i)

#pick only even numbers
for i in list2:
    if i % 2 == 0:
        newList.append(i)

newList.sort()
print("New list:",newList)
input("Exit")
