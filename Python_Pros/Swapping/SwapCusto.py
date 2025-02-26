def swap(a, b):
    return b, a  # Returning swapped values

a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(f"Before Swap: a = {a}, b = {b}")
a, b = swap(a, b)
print(f"After Swap: a = {a}, b = {b}")
