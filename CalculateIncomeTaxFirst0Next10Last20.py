print("Calculate income tax for the given income")
UserIncome = int(input("Your yearly income to calculate tax: "))
PayOrNot = True

def calculateIncome(UserIncome):
    if UserIncome <= 10000:
        PayOrNot = "No"
        return PayOrNot

    if UserIncome <= 20000:
        SecondTax = UserIncome - 10000
        SecondTax = (SecondTax / 100) * 10
        return SecondTax

    if UserIncome > 20000:
        SecondTax = (10000 / 100) * 10
        RemainingTax = UserIncome - 20000
        RemainingTax = (RemainingTax / 100) * 20
        OutputTax = RemainingTax + SecondTax
        return OutputTax



print("From income:", UserIncome, "Taxes:", calculateIncome(UserIncome), "taxes")
input("Exit")
