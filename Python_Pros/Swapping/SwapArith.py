a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(f"Before Swap: a = {a}, b = {b}")
a = a + b
b = a - b
a = a - b
print(f"After Swap: a = {a}, b = {b}")
