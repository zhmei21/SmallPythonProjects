string = "Bobby likes to write. Bobby is a good developer. I'm proud of Bobby."
x = 0

#cut the number of string given by user
listOfString = string.split()
for i in listOfString:
    if i == "Bobby":
        x += 1
print("Return the count of a given substring from a string \n")
print(string)
print("Bobby appeared", x, "times")

input("Exit")