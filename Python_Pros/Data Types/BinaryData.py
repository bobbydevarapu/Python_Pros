# Bytes (Immutable)
b = bytes([65, 66, 67])  # ASCII values of 'A', 'B', 'C'
print(b)  # Output: b'ABC'

# Bytearray (Mutable)
ba = bytearray(b)
ba[1] = 90  # Changing 'B' (66) to 'Z' (90)
print(ba)  # Output: bytearray(b'AZC')

# Memoryview (Accessing Binary Data)
mv = memoryview(b)
print(mv[0])  # Output: 65 (ASCII of 'A')
