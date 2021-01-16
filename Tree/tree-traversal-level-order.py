# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/


from collections import deque


class Node:

	# A utility function to create a new node
	def __init__(self, key):
		self.val = key 
		self.left = None
		self.right = None


def levelOrder(root):
    result=deque()
    
    if root is None:
        return []
    
    queue=deque([root])
    while len(queue) > 0:
        node = queue.popleft()
        if node:
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result


root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)
print("DFS traversal of binary tree is -")
print(levelOrder(root))
