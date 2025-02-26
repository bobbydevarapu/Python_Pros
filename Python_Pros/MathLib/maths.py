import math

# Taking user input
num = float(input("Enter a number: "))
angle = float(input("Enter an angle in degrees: "))

# Basic Math Operations
print("Ceil:", math.ceil(num))
print("Floor:", math.floor(num))
print("Absolute:", math.fabs(num))
print("Square Root:", math.sqrt(num))
print("Power:", math.pow(num, 2))

# Logarithmic Functions
print("Log (base e):", math.log(num))
print("Log (base 10):", math.log10(num))

# Trigonometric Functions
radian = math.radians(angle)
print("Sin:", math.sin(radian))
print("Cos:", math.cos(radian))
print("Tan:", math.tan(radian))

# Constants
print("Pi:", math.pi)
print("e:", math.e)
