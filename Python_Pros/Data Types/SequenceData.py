# List Operations
l1 = [1, 2, 3, 4, 5]
l1.append(6)     # Append element
l1.remove(3)     # Remove element
l1.insert(2, 10) # Insert at index 2
print(l1[:3])    # Slicing

# Tuple Operations
t1 = (10, 20, 30, 40, 50)
print(t1[1], t1[-1]) # Access elements

# Range Operations
r = range(1, 10, 2)  # Start=1, Stop=10, Step=2
print(list(r))       # Convert to list for display
print(sum(r))        # Calculate sum