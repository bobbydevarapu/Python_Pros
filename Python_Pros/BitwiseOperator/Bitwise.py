# Taking input from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Performing bitwise operations
print("\nBitwise Operations:")
print(f"{a} & {b}  (AND)         = {a & b}")   # Bitwise AND
print(f"{a} | {b}  (OR)          = {a | b}")   # Bitwise OR
print(f"{a} ^ {b}  (XOR)         = {a ^ b}")   # Bitwise XOR
print(f"~{a}  (NOT)            = {~a}")      # Bitwise NOT
print(f"{a} << 2 (Left Shift)  = {a << 2}")  # Left Shift
print(f"{a} >> 2 (Right Shift) = {a >> 2}")  # Right Shift


"""-----Explanation of Bitwise Operators--|
                                          |
✔ & → AND (1 if both bits are 1)          |
✔ | → OR (1 if at least one bit is 1)     |
✔ ^ → XOR (1 if bits are different)       |
✔ ~ → NOT (Flips all bits)                |
✔ << → Left Shift (Multiplies by 2^n)     |
✔ >> → Right Shift (Divides by 2^n)       |
"""