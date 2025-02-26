# Creating sets
print("\n")
s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}
print("Set 1:", s1)
print("Set 2:", s2)

# 1. Union - Combines elements from both sets
print("Union:", s1.union(s2))

# 2. Intersection - Finds common elements
print("Intersection:", s1.intersection(s2))

# 3. Difference - Elements in s1 but not in s2
print("Difference (s1 - s2):", s1.difference(s2))

# 4. Symmetric Difference - Elements in either set, but not both
print("Symmetric Difference:", s1.symmetric_difference(s2))

# 5. Adding an element
s1.add(60)
print("After adding 60 to s1:", s1)

# 6. Removing an element (removes if exists, else gives error)
s1.remove(10)  
print("After removing 10 from s1:", s1)

# 7. Discarding an element (removes if exists, no error if not)
s1.discard(100)  # No error even if 100 is not in the set
print("After discarding 100:", s1)

# 8. Checking if a set is a subset of another
print("Is s1 a subset of s2?", s1.issubset(s2))

# 9. Checking if a set is a superset of another
print("Is s1 a superset of s2?", s1.issuperset(s2))

# 10. Clearing the set
s1.clear()
print("After clearing s1:", s1)


""" Summary of Set Operations
1️⃣ Union (union()) :  Combines elements from both sets.
2️⃣ Intersection (intersection()) : Finds common elements.
3️⃣ Difference (difference()) : Elements in one set but not in another.
4️⃣ Symmetric Difference (symmetric_difference()) : Elements in either set but not both.
5️⃣ Add (add()) & Remove (remove()) : Modifies set elements.
6️⃣ Subset (issubset()) & Superset (issuperset()) : Checks set relationships."""