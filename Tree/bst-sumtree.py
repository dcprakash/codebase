"""
https://www.geeksforgeeks.org/check-if-a-given-binary-tree-is-sumtree/
"""

class node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
    
    
def sumTree(root):
    if root==None:
        return 0
    return sumTree(root.left) + root.data + sumTree(root.right)
        


def isSumTree(node):
    if not node or (node.left==None and node.right==None):
        return True
    
    ls=sumTree(node.left)
    rs=sumTree(node.right)

    if ((node.data==ls+rs) and
        isSumTree(node.left) and
        isSumTree(node.right)):
            return True
    else:
        return False

if __name__=='__main__':
    root=node(26)
    root.left= node(10)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(6)
    root.right.right = node(3)
    
    if(isSumTree(root)):
        print("The given tree is a SumTree ")
    else:
        print("The given tree is not a SumTree ")