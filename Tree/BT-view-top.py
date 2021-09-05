"""
https://leetcode.com/problems/binary-tree-vertical-order-traversal/solution/
Deque is preferred over list in the cases where we need quicker O(1) 
    append and pop operations from both the ends of container 
    deque.appendleft(6);also popleft
    deque.appendright(2); also popright
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
    # deque is like append, this adds root at 0th index
    queue = deque([(root, 0)])
    while queue:
        node, col = queue.popleft()
        
        if node:
            columntable[col].append(node.val)
            
            queue.append((node.left, col-1))
            queue.append((node.right, col+1))
    return ([columntable[x] for x in sorted(columntable.keys())])
    # columntable={0: [2, 1], -1: [9], 1: [8], -2: [4], 2: [7]})


root = Node(2)
root.left = Node(9)
root.right = Node(8)
root.left.left = Node(4)
root.right.left = Node(1)
root.right.right = Node(7)
print(topview(root))
