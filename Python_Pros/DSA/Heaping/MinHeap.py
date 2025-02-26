import heapq

# Creating a Min Heap
min_heap = []
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 20)
heapq.heappush(min_heap, 1)

print("Min Heap:", min_heap)  # Output: [1, 5, 20, 10] (Heap Property Maintained)

# Extracting the smallest element
print("Popped Element:", heapq.heappop(min_heap))  # Output: 1
print("Min Heap after pop:", min_heap)  # Output: [5, 10, 20]
