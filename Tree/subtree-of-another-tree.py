"""
https://leetcode.com/problems/subtree-of-another-tree/

duplicate tree
subtree within tree

similar to BT-duplicate-subtrees


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        tree1=[]
        tree2=[]
        
        def helper1(node):
            if not node:    return '#'
            serial="{},{},{}".format(node.val, helper1(node.left), helper1(node.right))
            tree1.append(serial)
            return serial
        
        def helper2(node):
            if not node:    return '#'
            serial="{},{},{}".format(node.val, helper1(node.left), helper1(node.right))
            tree2.append(serial)
            return serial
        
        helper1(root)
        helper2(subRoot)
        
        # print(tree1)
        # print(tree2)
        # ['1,#,#', '2,#,#', '4,1,#,#,2,#,#', '5,#,#', '3,4,1,#,#,2,#,#,5,#,#', '1,#,#', '2,#,#']
        # ['4,1,#,#,2,#,#']

        for tree in tree1:
            if tree in tree2:   return True
        return False