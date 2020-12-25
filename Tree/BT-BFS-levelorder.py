"""
Your module description
"""

# Recursive Python program for level 
# order traversal of Binary Tree

# A node structure
class Node:

	# A utility function to create a new node
	def __init__(self, key):
		self.data = key 
		self.left = None
		self.right = None

			
def LevelOrder(root):
    if not root:
        return None
    res=[]
    q=[]
    q.append(root)
    while q:
        tq=q.pop(0)
        res.append(tq.data)
        if tq.left:
            q.append(tq.left)
        if tq.right:
            q.append(tq.right)
    return res
        
        

# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level order traversal of binary tree is -")
print(LevelOrder(root))
