"""

https://leetcode.com/problems/kth-smallest-element-in-a-bst/solution/
It's a very straightforward approach with \mathcal{O}(N)O(N) time complexity.
    The idea is to build an inorder traversal of BST which is an array sorted in the ascending order. 
    Now the answer is the k - 1th element of this array.
"""

# A node structure
class Node:

	# A utility function to create a new node
	def __init__(self, key):
		self.data = key 
		self.left = None
		self.right = None


def kthSmallest(root, k):
    def inorder(r):
        return inorder(r.left) + [r.data] + inorder(r.right) if r else []

    return inorder(root)[k - 1]


# Driver program to test above function
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
k=5

# print(findDuplicateSubtrees(root))
print(kthSmallest(root, k))