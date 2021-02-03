# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/


from collections import deque


class Node:

	# A utility function to create a new node
	def __init__(self, key):
		self.data = key 
		self.left = None
		self.right = None

# uses BFS
def mergeTreeSum(root1, root2):
    if not root1:   return root2
    if not root2:   return root1
    tree = Node(root1.data + root2.data)
    tree.left = mergeTreeSum(root1.left, root2.left)
    tree.right = mergeTreeSum(root1.right, root2.right)
    return tree


def LevelOrder(root):
    if not root:
        return None
    res=[]
    q=[]
    q.append(root)
    while q:
        tq=q.pop(0)
        res.append(tq.data)
        if tq.left:
            q.append(tq.left)
        if tq.right:
            q.append(tq.right)
    return res


root1 = Node(4)
root1.left = Node(1)
root1.right = Node(0)
root1.left.left = Node(5)

root2 = Node(2)
root2.left = Node(3)
root2.right = Node(4)
root2.right.left = Node(5)

tree=mergeTreeSum(root1, root2)
print(LevelOrder(tree))
