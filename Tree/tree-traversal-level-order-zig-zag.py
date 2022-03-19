# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/


from collections import deque


class Node:
	# A utility function to create a new node
	def __init__(self, key):
		self.val = key 
		self.left = None
		self.right = None


def levelOrder(root):
    
    if root is None:
        return []
    
    ret=[]
    result=deque()
    queue=deque([root, None])   # added None after root, to create None delimited levels to tell we finished one level
    is_left = True
    
    while len(queue) > 0:
        node = queue.popleft()
        if node:
            if is_left: result.appendleft(node.val)
            else:   result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        else:
            ret.append(result)
            if len(queue) > 0:
                queue.append(None) # add None to delimiate next level
            result = deque()
            is_left = not is_left
    return ret


root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)
print("DFS traversal of binary tree is -")
print(levelOrder(root))
