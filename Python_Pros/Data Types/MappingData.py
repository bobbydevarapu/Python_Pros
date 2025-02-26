# Dictionary Operations
d = {'name': 'Alice', 'age': 25, 'city': 'New York'}
d['age'] = 26         # Update value
d['gender'] = 'F'     # Add new key-value pair
del d['city']         # Delete key-value pair

print(d.keys())       # Get all keys
print(d.values())     # Get all values
print(d.items())      # Get key-value pairs
print(d.get('name'))  # Access value safely
