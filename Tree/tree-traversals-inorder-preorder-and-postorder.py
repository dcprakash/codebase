"""
inorder
preorder
postorder
Tree example: https://www.geeksforgeeks.org/find-k-th-smallest-element-in-bst-order-statistics-in-bst/
use DFS to traverse tree
"""

# A node structure
class Node:

	# A utility function to create a new node
	def __init__(self, key):
		self.data = key 
		self.left = None
		self.right = None


def preorderTraverse(root):
    def preorder(r):
        return [r.data] + preorder(r.left) + preorder(r.right) if r else []

    return preorder(root)


def inorderTraverse(root):
    def inorder(r):
        return inorder(r.left) + [r.data] + inorder(r.right) if r else []

    return inorder(root)


def postorderTraverse(root):
    def postorder(r):
        return postorder(r.left) + postorder(r.right) + [r.data] if r else []

    return postorder(root)


# Driver program to test above function
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
k=5


print("Preorder traversals of tree ")
print(preorderTraverse(root))

# print(findDuplicateSubtrees(root))
print("\n Inorder traversals of tree ")
print(inorderTraverse(root))

print("\n Postorder traversals of tree ")
print(postorderTraverse(root))
