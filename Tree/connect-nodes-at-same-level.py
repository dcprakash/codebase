"""
https://www.geeksforgeeks.org/connect-nodes-at-same-level/
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
		self.nextright = None

			
def LevelOrder(root):
    if not root:
        return None
    res=[]
    q=[]
    q.append(root)
    temp=Node(None)
    while q:
        n=len(q)
        for i in range(n):
            prv=temp
            tq=q.pop(0)
            if i>0:
                prv.nextright=temp
            res.append(tq.data)
            if tq.left:
                q.append(tq.left)
            if tq.right:
                q.append(tq.right)
        temp.nextright=None
    return res
        
        

# Driver program to test above function
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

print("Level order traversal of binary tree is -")
print(LevelOrder(root))
print("Next right of {} is {}".format(root.left.data, root.left.nextright.data))