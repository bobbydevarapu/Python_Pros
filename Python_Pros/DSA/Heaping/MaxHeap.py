import heapq

# Creating a Max Heap using negative values
max_heap = []
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -20)
heapq.heappush(max_heap, -1)

# Convert back to positive for display
print("Max Heap:", [-i for i in max_heap])  # Output: [20, 10, 5, 1]

# Extracting the largest element
print("Popped Element:", -heapq.heappop(max_heap))  # Output: 20
print("Max Heap after pop:", [-i for i in max_heap])  # Output: [10, 1, 5]
