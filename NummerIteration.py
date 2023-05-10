print("Printing current and previous number sum in a range(10)")
num1 = 0
num2 = 0
summ = 0
#make a number iteration and print it out
for i in range(10):
    print("Current Number: ", num1, "Previous Number: ", num2, "Sum: ", summ)
    num1 += 1
    num2 = num1 - 1
    summ = num1 + num2

input("Exit")
