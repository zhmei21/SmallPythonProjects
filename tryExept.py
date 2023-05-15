import sys

print("Try and except errors")
print("Start: 4 Divide: ?")

try:
    x = int(input("Give a number: "))
    print("Ergebnis: ", 4/x)
except ZeroDivisionError:
    print("Please no zero")
except ValueError:
    print("Please a number")
except:
    print("A wild bug has appeared:", sys.exc_info()[0])
else:
    print("Program ran successful. No error")
#finally:

input("Exit")

