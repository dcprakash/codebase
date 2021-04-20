"""
Your module description
"""

# Recursive Python program for DFS traversal of Binary Tree

# A node structure
class Node:

	# A utility function to create a new node
	def __init__(self, key):
		self.data = key 
		self.left = None
		self.right = None


def dfs(root):
    return [root.data] + dfs(root.left) + dfs(root.right) if root else []

			
def DFS_global(root):
    if not root:
        return None
    global res
    res.append(root.data)
    if root.left:
        DFS_global(root.left)
    if root.right:
        DFS_global(root.right)
    return res

        
def DFS_noglobal(root,result):
    if not root:
        return None
    result.append(root.data)
    if root.left:
        DFS_noglobal(root.left,result)
    if root.right:
        DFS_noglobal(root.right,result)
    return result


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
res = []
print("DFS traversal of binary tree is -")
print(dfs(root))
print(DFS_global(root))
print(DFS_noglobal(root, []))
