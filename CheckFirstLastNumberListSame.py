numbers_y = [76, 43, 19, 60, 45]
numbers_x = [10, 27, 32, 60, 10]

#remove the first and last number and checks if the same
def checkNumbers(numbers):
    TrueOrFalse = True
    numberOne = numbers.pop(0)
    numberTwo = numbers.pop(-1)
    if numberOne == numberTwo:
        return TrueOrFalse
    else:
        TrueOrFalse = False
        return TrueOrFalse
    
print("Check if the first and last number of a list is the same \n")    
print(numbers_x)
print(checkNumbers(numbers_x), "\n")
print(numbers_y)
print(checkNumbers(numbers_y), "\n")

input("Exit")
