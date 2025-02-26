# Set Operations
s1 = {1, 2, 3, 4, 5}
s1.add(6)       # Add element
s1.remove(3)    # Remove element
s2 = {4, 5, 6, 7, 8}
print(s1.union(s2))   # Union of sets
print(s1.intersection(s2))  # Intersection of sets
print(s1.difference(s2))    # Difference

# Frozenset Operations
fs = frozenset([10, 20, 30])
print(fs)  # Frozenset (immutable)
