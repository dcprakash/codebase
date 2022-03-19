"""
Your module description
"""

# Recursive Python program for level 
# order traversal of Binary Tree
# queue - FIFO
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
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

print("Level order traversal of binary tree is -")
print(LevelOrder(root))
