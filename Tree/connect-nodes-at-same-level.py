"""
https://www.geeksforgeeks.org/connect-nodes-at-same-level/
"""

# Recursive Python program for level 
# order traversal of Binary Tree
# Method 2 (Extend Pre Order Traversal) 


# A node structure
from operator import le


class Node:

	# A utility function to create a new node
	def __init__(self, key):
		self.data = key 
		self.left = None
		self.right = None
		self.nextright = None

			
def LevelOrder(root):
    if not root:
        return None
    q=[]
    q.append(root)
    while q:
        prv=Node(None)
        for _ in range(len(q)):
            tq=q.pop(0)
            if tq.left:
                q.append(tq.left)
            if tq.right:
                q.append(tq.right)
            if prv is not None:
                prv.nextright=tq
            prv=tq
        prv.nextright=None
        
        

# Driver program to test above function
root = Node(3)
root.left = Node(9)
root.right = Node(20)
# root.right.left = Node(15)
# root.right.right = Node(7)

print("Level order traversal of binary tree is -")
print(LevelOrder(root))
print("Next right of {} is {}".format(root.left.data, root.left.nextright.data))
# print("Next right of {} is {}".format(root.right.data, root.right.nextright.data))