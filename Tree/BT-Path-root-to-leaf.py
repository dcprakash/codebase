"""
https://leetcode.com/problems/binary-tree-paths/solution/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.res=[]
        
        def btPath(node,path):
            if not node:
                return []
            
            path+=str(node.val)
            
            if not node.left and not node.right:
                self.res.append(path)
            else:
                path+="->"
                btPath(node.left,path)
                btPath(node.right,path)
                
            return self.res
        
        
        btPath(root,'')
        return self.res
"""
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
def pathToLeaf(root, path):
	global res
	if not root:
		return []
	else:
		path+=str(root.data)
		if not root.left and not root.right:
			res.append(path)
		else:
			path+='->'
			pathToLeaf(root.left, path)
			pathToLeaf(root.right, path)
	return res
        
        

# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
res=[]
print(pathToLeaf(root, ''))


        