print("extract each digit from an integer in the reverse order.")
userInput = input("Please give a integer to reverse: ")
emptyList = []
for i in userInput:
    emptyList.append(i)
newList = emptyList[::-1]
print(' '.join(newList))

input("Exit")