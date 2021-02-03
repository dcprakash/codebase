# Python program to find if two trees are mirror 
# https://www.geeksforgeeks.org/check-if-two-trees-are-mirror/

# A Binary Tree Node 
class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None


def mirror(root1, root2):
    # Base case : Both empty
    if root1==None and root2==None: return True
    # Base case : only one empty
    if root1==None or root2==None: return True
    return (mirror(root1.left, root2.right) and mirror(root1.right, root2.left)) if root1.data==root2.data else False


# Driver program 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3); 
root.left.left = Node(4); 
root.left.right = Node(5); 

root2 = Node(1) 
root2.left = Node(3) 
root2.right = Node(2); 
root2.right.left = Node(5); 
root2.right.right = Node(4); 

print(mirror(root, root2))
