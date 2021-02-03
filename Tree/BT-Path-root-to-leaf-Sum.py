# https://leetcode.com/problems/sum-root-to-leaf-numbers/solution/

class Node:

	# A utility function to create a new node
	def __init__(self, key):
		self.data = key 
		self.left = None
		self.right = None
        
    
def sumNumbers(root):
    root_to_leaf = 0
    stack = [(root, 0) ]
    
    while stack:
        root, curr_number = stack.pop()
        if root is not None:
            curr_number = curr_number * 10 + root.data
            # if it's a leaf, update root-to-leaf sum
            if root.left is None and root.right is None:
                root_to_leaf += curr_number
            else:
                stack.append((root.right, curr_number))
                stack.append((root.left, curr_number))
                    
    return root_to_leaf


root = Node(4)
root.left = Node(9)
root.right = Node(0)
root.left.left = Node(5)
root.left.right = Node(1)
print(sumNumbers(root))
