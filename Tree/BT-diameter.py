"""
https://leetcode.com/problems/diameter-of-binary-tree/

You will see we are going to address them by 
1) applying DFS to recursively find the longest branches starting with the node's left and right children; 
2) initializing a global variable diameter to keep track of the longest path and updating it at each node
    with the sum of the node's left and right branches; 
3) returning the length of the longest branch between a node's left and right branches.

Algorithm
Initalize an integer variable diameter to keep track of the longest path we find from the DFS.
Implement a recursive function longestPath which takes a TreeNode as input. 
    It should recursively explore the entire tree rooted at the given node. 
    Once it's finished, it should return the longest path out of its left and right branches:
if node is None, we have reached the end of the tree, hence we should return 0;
we want to recursively explore node's children, so we call longestPath again with node's left and right children. 
    In return, we get the longest path of its left and right children leftPath and rightPath;
if leftPath plus rightPath is longer than the current longest diameter found, then we need to update diameter;
finally, we return the longer one of leftPath and rightPath. Remember to add 11 as the edge connecting it with its parent.
Call longestPath with root.

"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    import math
    def diameterOfBinaryTree(self, root):
        self.ans=1
        
        def helper(node):
            if not node:
                return 0
            L=helper(node.left)
            R=helper(node.right)
            self.ans=max(self.ans, L+R+1)
            return max(L,R)+1
            
        helper(root)
        return self.ans-1
        

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
s=Solution()
print(s.diameterOfBinaryTree(root))