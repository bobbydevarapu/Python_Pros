# Creating a dictionary
d1 = {"name": "Alice", "age": 25, "city": "New York"}
print("Original Dictionary:", d1)

# 1. Accessing values
print("Name:", d1["name"])  # Using key
print("Age:", d1.get("age"))  # Using get()

# 2. Adding a new key-value pair
d1["country"] = "USA"
print("After Adding Country:", d1)

# 3. Updating an existing value
d1["age"] = 26
print("After Updating Age:", d1)

# 4. Removing a key-value pair
d1.pop("city")
print("After Removing City:", d1)

# 5. Checking if a key exists
print("Is 'name' in dictionary?", "name" in d1)

# 6. Getting all keys
print("Keys:", d1.keys())

# 7. Getting all values
print("Values:", d1.values())

# 8. Getting all key-value pairs
print("Items:", d1.items())

# 9. Merging another dictionary
d2 = {"gender": "Female", "hobby": "Reading"}
d1.update(d2)
print("After Merging:", d1)

# 10. Removing all elements
d1.clear()
print("After Clearing Dictionary:", d1)


""" 📌 Summary of Dictionary Operations
1️⃣ Accessing Values: dict[key], dict.get(key)
2️⃣ Adding & Updating Values: dict[key] = value
3️⃣ Removing Elements: pop(key), del dict[key], clear()
4️⃣ Checking Key Existence: "key" in dict
5️⃣ Getting Keys, Values, Items: keys(), values(), items()
6️⃣ Merging Dictionaries: update()
"""