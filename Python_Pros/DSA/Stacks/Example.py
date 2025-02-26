class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):  # Add element
        self.stack.append(item)

    def pop(self):  # Remove last element
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):  # View top element
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):  # Check if empty
        return len(self.stack) == 0

    def display(self):  # Print stack
        print("Stack:", self.stack)

# Example Usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()  # Output: Stack: [10, 20, 30]
print(s.pop())  # Output: 30
print(s.peek())  # Output: 20
s.display()  # Output: Stack: [10, 20]
print(s.is_empty())  # Output: False
