print("Check if Palindrome number")
check = int(input("Check your number "))
print("Your original number", check)

#change the number to string, invert it and change back to int
reverse = str(check)[::-1]
reverseNum = int(reverse)

if reverseNum == check:
    print("Yes. Given number is palindrome number.")
else:
    print("No. Given number is not palindrome number.")

input("Exit")
