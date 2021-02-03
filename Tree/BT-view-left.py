from queue import Queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/binary-tree-right-side-view/solution/


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


import math
import queue

def rightView(root):
    result = []
    if root:
        q = queue.Queue()
        q.put_nowait((root, 0))
        while not q.empty():
            node, d = q.get_nowait()
            if len(result) == d:
                result.append(node.data)
            for child in (node.left, node.right, ):
                if child:
                    q.put_nowait((child, d + 1))
    return result
		
        
        

# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
res=[]
print(rightView(root))
