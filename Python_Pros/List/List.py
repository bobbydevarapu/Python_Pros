# Creating a list
l1 = [10, 20, 30, 40, 50]
print("Initial List:", l1)

# 1. Append - Adds an element to the end
l1.append(60)
print("After append(60):", l1)

# 2. Insert - Adds an element at a specific index
l1.insert(2, 25)  # Insert 25 at index 2
print("After insert(2, 25):", l1)

# 3. Remove - Removes the first occurrence of the specified value
l1.remove(30)
print("After remove(30):", l1)

# 4. Pop - Removes and returns the last element (or element at a given index)
popped_value = l1.pop()  # Removes last element
print("After pop():", l1, "(Removed:", popped_value, ")")
popped_index_value = l1.pop(2)  # Removes element at index 2
print("After pop(2):", l1, "(Removed:", popped_index_value, ")")

# 5. Sort - Sorts the list in ascending order
l1.sort()
print("After sort():", l1)

# 6. Reverse - Reverses the list
l1.reverse()
print("After reverse():", l1)

# 7. Index - Finds the index of the first occurrence of an element
index_40 = l1.index(40)
print("Index of 40:", index_40)

# 8. Count - Counts occurrences of an element
count_20 = l1.count(20)
print("Count of 20:", count_20)

# 9. Copy - Creates a copy of the list
l2 = l1.copy()
print("Copied List (l2):", l2)

# 10. Extend - Extends list by adding elements from another list
l3 = [70, 80, 90]
l1.extend(l3)
print("After extend([70, 80, 90]):", l1)

# 11. Clear - Removes all elements from the list
l1.clear()
print("After clear():", l1)

# 12. Del - Deletes the list completely
del l1
print("List deleted successfully!")


""" :-----------lists in Python----------:  

1️. Lists are mutable  :You can modify them by adding, removing, or changing elements.  

2️ .Lists allow duplicate values : A list can store multiple occurrences of the same value. """