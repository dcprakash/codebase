{"filter":false,"title":"BT-Path-root-to-leaf.py","tooltip":"/Tree/BT-Path-root-to-leaf.py","undoManager":{"mark":3,"position":3,"stack":[[{"start":{"row":1,"column":0},"end":{"row":1,"column":23},"action":"remove","lines":["Your module description"],"id":2},{"start":{"row":1,"column":0},"end":{"row":1,"column":57},"action":"insert","lines":["https://leetcode.com/problems/binary-tree-paths/solution/"]}],[{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":3}],[{"start":{"row":4,"column":0},"end":{"row":32,"column":8},"action":"insert","lines":["# Definition for a binary tree node.","# class TreeNode:","#     def __init__(self, val=0, left=None, right=None):","#         self.val = val","#         self.left = left","#         self.right = right","class Solution:","    def binaryTreePaths(self, root: TreeNode) -> List[str]:","        self.res=[]","        ","        def btPath(node,path):","            if not node:","                return []","            ","            path+=str(node.val)","            ","            if not node.left and not node.right:","                self.res.append(path)","            else:","                path+=\"->\"","                btPath(node.left,path)","                btPath(node.right,path)","                ","            return self.res","        ","        ","        btPath(root,'')","        return self.res","        "],"id":4}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":2},"action":"remove","lines":["# "],"id":5},{"start":{"row":6,"column":0},"end":{"row":6,"column":2},"action":"remove","lines":["# "]},{"start":{"row":7,"column":0},"end":{"row":7,"column":2},"action":"remove","lines":["# "]},{"start":{"row":8,"column":0},"end":{"row":8,"column":2},"action":"remove","lines":["# "]}],[{"start":{"row":11,"column":45},"end":{"row":11,"column":58},"action":"remove","lines":[" -> List[str]"],"id":6}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":5,"column":15},"end":{"row":5,"column":15},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1608920453172,"hash":"8a6711b24e667da03a7f58b99f55beaeddedb3a9"}