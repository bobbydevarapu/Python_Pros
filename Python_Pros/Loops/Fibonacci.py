n = int(input("Enter n: "))  # Number of terms
F1 = int(input("Enter F1: "))  # First Fibonacci number
F2 = int(input("Enter F2: "))  # Second Fibonacci number
print()
print("Fibonacci numbers are: ")
for i in range(n):
    print(F1, end=" ")  # Print the current Fibonacci number
    F1, F2 = F2, F1 + F2  # Update values for the next iteration
    