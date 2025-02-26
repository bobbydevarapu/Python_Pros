# Arithmetic Operators
a = 10
b = 5
print("\n")
print("Arithmetic Operators:")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}\n")

# Comparison Operators
print("Comparison Operators:")
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
print(f"{a} >= {b}: {a >= b}")
print(f"{a} <= {b}: {a <= b}\n")

# Logical Operators
x, y = True, False
print("Logical Operators:")
print(f"x and y: {x and y}")
print(f"x or y: {x or y}")
print(f"not x: {not x}\n")

# Bitwise Operators
m, n = 6, 3  # 6 = 110, 3 = 011 in binary
print("Bitwise Operators:")
print(f"m & n: {m & n}")  # AND
print(f"m | n: {m | n}")  # OR
print(f"m ^ n: {m ^ n}")  # XOR
print(f"~m: {~m}")  # NOT
print(f"m << 1: {m << 1}")  # Left Shift
print(f"m >> 1: {m >> 1}\n")  # Right Shift

# Assignment Operators
c = 10
print("Assignment Operators:")
c += 2
print(f"c += 2: {c}")
c -= 2
print(f"c -= 2: {c}")
c *= 2
print(f"c *= 2: {c}")
c /= 2
print(f"c /= 2: {c}\n")

# Identity Operators
p = [1, 2, 3]
q = p
r = [1, 2, 3]
print("Identity Operators:")
print(f"p is q: {p is q}")  # True, same object
print(f"p is r: {p is r}")  # False, different objects
print(f"p is not r: {p is not r}\n")

# Membership Operators
print("Membership Operators:")
print(f"2 in p: {2 in p}")
print(f"4 not in p: {4 not in p}")


""" 
|----------Operators in Python----------------------|
                                                
Arithmetic Operators (+, -, *, /, //, %, **)
Comparison (Relational) Operators (==, !=, >, <, >=, <=)
Logical Operators (and, or, not)
Bitwise Operators (&, |, ^, ~, <<, >>)
Assignment Operators (=, +=, -=, *=, /=, //=, %=, **=)
Identity Operators (is, is not)
Membership Operators (in, not in)

"""