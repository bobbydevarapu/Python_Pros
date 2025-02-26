def bit_operations(n):
    print(f"Binary representation: {bin(n)}")

    # AND operation (Check if even or odd)
    print("Even" if (n & 1) == 0 else "Odd")

    # OR operation (Set a bit at position 1)
    pos = 1
    print(f"Setting bit at position {pos}: {bin(n | (1 << pos))}")

    # XOR operation (Toggle bit at position 1)
    print(f"Toggling bit at position {pos}: {bin(n ^ (1 << pos))}")

    # NOT operation (Bitwise negation)
    print(f"Bitwise NOT: {bin(~n)}")

    # Left shift (Multiply by 2)
    print(f"Left shift (n << 1): {n << 1}")

    # Right shift (Divide by 2)
    print(f"Right shift (n >> 1): {n >> 1}")

    # Count set bits
    print(f"Number of 1s in binary: {bin(n).count('1')}")

# Take user input
num = int(input("Enter a number: "))
bit_operations(num)
