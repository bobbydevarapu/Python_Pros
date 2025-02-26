# Taking input from the user
num = int(input("Enter a number: "))

# Checking conditions using if-elif-else
if num > 0:
    print("The number is Positive")
    if num % 2 == 0:
        print("It is an Even number")
    else:
        print("It is an Odd number")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")
