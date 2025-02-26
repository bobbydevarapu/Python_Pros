class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):  # Add element to the queue
        self.queue.append(item)

    def dequeue(self):  # Remove first element from the queue
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty"

    def peek(self):  # View front element
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty"

    def is_empty(self):  # Check if empty
        return len(self.queue) == 0

    def display(self):  # Print queue
        print("Queue:", self.queue)

# Example Usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()  # Output: Queue: [10, 20, 30]
print(q.dequeue())  # Output: 10
print(q.peek())  # Output: 20
q.display()  # Output: Queue: [20, 30]
print(q.is_empty())  # Output: False