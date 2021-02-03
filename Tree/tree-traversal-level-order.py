# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/


from collections import deque


class Node:

	# A utility function to create a new node
	def __init__(self, key):
		self.data = key 
		self.left = None
		self.right = None


def levelOrder(root):
    levels=[]
    if not root:    return levels
    def helper(root, depth):
        if len(levels)==depth:
            levels.append([])
        levels[depth].append(root.data)
        if root.left:   helper(root.left, depth+1)
        if root.right:  helper(root.right, depth+1)
    helper(root, 0)
    return levels


root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)
print("DFS traversal of binary tree is -")
print(levelOrder(root))
