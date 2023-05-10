print("Calculate the multiplication and sum of two numbers \n")
loop = 3

#multiply the users input
def multipli(userInput1, userInput2):
    summ = userInput1 * userInput2
    return summ

#add the users input
def addier(userInput1, userInput2):
    summ = userInput1 + userInput2
    return summ

#a choose menu
while(loop == 3):
    userInput1 = int(input("Give a number: "))
    userInput2 = int(input("Give a second number: "))
    userInput3 = int(input("Do you want to Multiply :1 Or Addition :2 Or Stop :0 | "))

    if userInput3 == 1:
        print("summ: ", multipli(userInput1, userInput2))
        loop = int(input("Continue: Y = 3 / N = 0 : "))


    if userInput3 == 2:
        print("summ: ", addier(userInput1, userInput2))
        loop = int(input("Continue: Y = 3 / N = 0 : "))

    if userInput3 == 0:
        print("See you soon!")
        break

input("Exit")
