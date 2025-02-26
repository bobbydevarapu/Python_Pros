# Creating a hash table using a dictionary
hash_table = {}

# Inserting key-value pairs
hash_table["name"] = "Alice"
hash_table["age"] = 25
hash_table["city"] = "New York"

# Accessing values
print("Name:", hash_table["name"])  # Output: Alice
print("Age:", hash_table.get("age"))  # Output: 25

# Deleting a key
del hash_table["city"]

# Checking if a key exists
print("Is 'city' in hash table?", "city" in hash_table)  # Output: False
