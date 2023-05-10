print("Print characters from a string that are present at an even index number \n")
userInput = input("Give a string: ")
print("Orginal String is ", userInput)
print("Printing only even index chars: ")
stringList = []
index = 0

#take the user input and put it into a string
for i in userInput:
    stringList.append(i)
    
#check for every index if its a even number and print it out
for i in range(len(stringList)):
    if i % 2 == 0:
        print(stringList[i])

input("Exit")
