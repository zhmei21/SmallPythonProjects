removeList = []
print("Remove first n characters from a string \n")
userInput = input("Give a string: ")
remove = int(input("How many to remove from the start? "))

#add the user input into a string for removal
for i in userInput:
    removeList.append(i)
    
#take the users second input to remove from the list and return the value. Also checks if given a number that can't be sliced 
if remove < len(removeList):
    def remove_chars(userInput, remove):
        del removeList[0:remove]
        newInput = ''.join(removeList)
        return newInput
    print("String: ", userInput, "| Remote number: ", remove, "| Output: ", remove_chars(userInput, remove))
else:
    print("Can't slice")

input("Exit")
