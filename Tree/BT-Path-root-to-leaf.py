"""
https://leetcode.com/problems/binary-tree-paths/solution/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.res=[]
        
        def btPath(node,path):
            if not node:
                return []
            
            path+=str(node.val)
            
            if not node.left and not node.right:
                self.res.append(path)
            else:
                path+="->"
                btPath(node.left,path)
                btPath(node.right,path)
                
            return self.res
        
        
        btPath(root,'')
        return self.res
        