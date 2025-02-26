class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, key):
        if key < self.value:
            if self.left:
                self.left.insert(key)
            else:
                self.left = BST(key)
        else:
            if self.right:
                self.right.insert(key)
            else:
                self.right = BST(key)

# Function to perform inorder traversal
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=" ")  # Print node value
        inorder_traversal(node.right)

# Example Usage
root = BST(10)
root.insert(5)
root.insert(15)
root.insert(2)
root.insert(7)

print("Inorder Traversal of BST:")
inorder_traversal(root)  # Output: 2 5 7 10 15
