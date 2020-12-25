"""
https://leetcode.com/problems/binary-tree-vertical-order-traversal/solution/

"""


from collections import defaultdict, deque


class Node:
	# A utility function to create a new node
	def __init__(self, key):
		self.val = key 
		self.left = None
		self.right = None

			
def topview(root):
    columntable = defaultdict(list)
    queue = deque([(root, 0)])
    while queue:
        node, col = queue.popleft()
        
        if node:
            columntable[col].append(node.val)
            
            queue.append((node.left, col-1))
            queue.append((node.right, col+1))
    return ([columntable[x] for x in sorted(columntable.keys())])
    


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
res = []
print("DFS traversal of binary tree is -")
print(topview(root))
