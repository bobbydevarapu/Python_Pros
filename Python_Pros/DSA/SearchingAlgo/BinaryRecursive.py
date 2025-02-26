def binary_search_recursive(arr, left, right, target):
    if left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, mid + 1, right, target)
        else:
            return binary_search_recursive(arr, left, mid - 1, target)
    return -1

arr = [10, 20, 30, 40, 50]
target = 30
print(binary_search_recursive(arr, 0, len(arr) - 1, target))  # Output: 2
