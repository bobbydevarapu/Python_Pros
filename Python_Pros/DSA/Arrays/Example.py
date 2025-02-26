# Array Operations in Python

from array import array
# Creating an array
arr = array('i', [1, 2, 3, 4, 5])
print("Original Array:", arr.tolist())

# Insertion
arr.insert(2, 10)  # Insert 10 at index 2
print("After Insertion:", arr.tolist())

# Deletion
arr.remove(3)  # Remove element 3
print("After Deletion:", arr.tolist())

# Searching
index = arr.index(4)  # Find index of element 4
print("Index of 4:", index)

# Updating
arr[1] = 20  # Update index 1 to 20
print("After Update:", arr.tolist())

# Traversing
print("Traversing the array:", [x for x in arr])
