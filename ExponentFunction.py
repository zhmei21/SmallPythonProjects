print("A function called exponent(userInputBase, userInputExp) that returns an int value of base raises to the power of exp.")
userInputBase = int(input("Give a base number: "))
userInputExp = int(input("Give a exponent: "))

def exponent(userInputBase, userInputExp):
    output = pow(userInputBase, userInputExp)
    return output
print(userInputBase, "raise to the power of",userInputExp,":",exponent(userInputBase, userInputExp))
