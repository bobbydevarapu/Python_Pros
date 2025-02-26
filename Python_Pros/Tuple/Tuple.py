# Creating a tuple
t1 = (10, 20, 30, 40, 50, 20)
print("Initial Tuple:", t1)

# 1. Indexing - Accessing elements using index
print("Element at index 2:", t1[2])

# 2. Slicing - Extracting a portion of the tuple
print("Slice from index 1 to 4:", t1[1:4])

# 3. Concatenation - Joining two tuples
t2 = (60, 70, 80)
t3 = t1 + t2
print("After concatenation:", t3)

# 4. Repetition - Repeating elements in a tuple
t4 = t1 * 2
print("After repetition:", t4)

# 5. Count - Counting occurrences of an element
count_20 = t1.count(20)
print("Count of 20:", count_20)

# 6. Index - Finding the first occurrence of an element
index_40 = t1.index(40)
print("Index of 40:", index_40)

# 7. Length - Finding the number of elements
print("Length of t1:", len(t1))

# 8. Membership - Checking if an element exists
print("Is 30 in t1?", 30 in t1)
print("Is 100 in t1?", 100 in t1)

# 9. Converting tuple to list (to modify elements)
list_from_tuple = list(t1)
list_from_tuple.append(90)  # Now modification is possible
t5 = tuple(list_from_tuple)
print("Modified Tuple after converting to list and adding 90:", t5)

# 10. Tuple Unpacking - Assigning elements to variables
a, b, c, d, e, f = t1  # Unpacking
print("Unpacked values:", a, b, c, d, e, f)



""" 
1️. Tuples are immutable : Once created, their elements cannot be changed, added, or removed.

2️ .Tuples support indexing and slicing : You can access elements using indexes and extract sub-tuples using slicing.
"""