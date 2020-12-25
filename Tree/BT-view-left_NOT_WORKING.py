"""
https://leetcode.com/problems/binary-tree-right-side-view/solution/
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
    global leftview
    while node.left!=None:
        leftview.append(node.data)
        node=node.left
    leftview.append(node.data)
    return leftview
        


if __name__=='__main__':
    leftview = []
    root=node(26)
    root.left= node(10)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(6)
    root.right.right = node(3)
    
    print(isSumTree(root))