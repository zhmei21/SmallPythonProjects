from datetime import datetime, time
userName = input("Hello User, what should i call you? ")
userAge = int(input("How old are you? "))

timeNow = int(datetime.today().year)


def calculateAge(timeNow, userAge):
    NowTime = timeNow - userAge + 100
    return NowTime


print("Hello", userName, "in year", calculateAge(
    timeNow, userAge), "you will be 100 years old.")

input('Press ENTER to exit')
