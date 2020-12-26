{"filter":false,"title":"bst-validate.py","tooltip":"/Tree/bst-validate.py","undoManager":{"mark":43,"position":43,"stack":[[{"start":{"row":3,"column":0},"end":{"row":8,"column":25},"action":"insert","lines":["# Definition for a binary tree node.","class TreeNode:","    def __init__(self, val=0, left=None, right=None):","        self.val = x","        self.left = None","        self.right = None"],"id":1}],[{"start":{"row":8,"column":25},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":9,"column":0},"end":{"row":9,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":9,"column":8},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":3},{"start":{"row":10,"column":0},"end":{"row":10,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":10,"column":4},"end":{"row":10,"column":8},"action":"remove","lines":["    "],"id":4},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":10,"column":0},"end":{"row":25,"column":29},"action":"insert","lines":["class Solution:","    def isValidBST(self, root: TreeNode) -> bool:","        ","        def validate(node, low=-math.inf, high=math.inf):","            # Empty trees are valid BSTs.","            if not node:","                return True","            # The current node's value must be between low and high.","            if node.val <= low or node.val >= high:","                return False","            ","            # The left and right subtree must also be valid.","            return (validate(node.right, node.val, high) and","                   validate(node.left, low, node.val))","        ","        return validate(root)"],"id":5}],[{"start":{"row":11,"column":40},"end":{"row":11,"column":48},"action":"remove","lines":[" -> bool"],"id":6}],[{"start":{"row":11,"column":30},"end":{"row":11,"column":39},"action":"remove","lines":[" TreeNode"],"id":7},{"start":{"row":11,"column":29},"end":{"row":11,"column":30},"action":"remove","lines":[":"]}],[{"start":{"row":11,"column":25},"end":{"row":11,"column":26},"action":"insert","lines":["i"],"id":8},{"start":{"row":11,"column":26},"end":{"row":11,"column":27},"action":"insert","lines":["n"]},{"start":{"row":11,"column":27},"end":{"row":11,"column":28},"action":"insert","lines":["t"]}],[{"start":{"row":11,"column":28},"end":{"row":11,"column":29},"action":"insert","lines":[" "],"id":9}],[{"start":{"row":11,"column":28},"end":{"row":11,"column":29},"action":"remove","lines":[" "],"id":10},{"start":{"row":11,"column":27},"end":{"row":11,"column":28},"action":"remove","lines":["t"]},{"start":{"row":11,"column":26},"end":{"row":11,"column":27},"action":"remove","lines":["n"]},{"start":{"row":11,"column":25},"end":{"row":11,"column":26},"action":"remove","lines":["i"]}],[{"start":{"row":11,"column":25},"end":{"row":11,"column":26},"action":"insert","lines":["T"],"id":11},{"start":{"row":11,"column":26},"end":{"row":11,"column":27},"action":"insert","lines":["r"]},{"start":{"row":11,"column":27},"end":{"row":11,"column":28},"action":"insert","lines":["e"]}],[{"start":{"row":11,"column":25},"end":{"row":11,"column":28},"action":"remove","lines":["Tre"],"id":12},{"start":{"row":11,"column":25},"end":{"row":11,"column":33},"action":"insert","lines":["TreeNode"]}],[{"start":{"row":11,"column":33},"end":{"row":11,"column":34},"action":"insert","lines":[" "],"id":13}],[{"start":{"row":3,"column":36},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":14}],[{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":15}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":33},"action":"insert","lines":["from dataclasses import dataclass"],"id":16}],[{"start":{"row":3,"column":33},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":17}],[{"start":{"row":5,"column":36},"end":{"row":6,"column":0},"action":"remove","lines":["",""],"id":18}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":36},"action":"remove","lines":["# Definition for a binary tree node."],"id":19},{"start":{"row":5,"column":0},"end":{"row":5,"column":1},"action":"insert","lines":["@"]},{"start":{"row":5,"column":1},"end":{"row":5,"column":2},"action":"insert","lines":["D"]},{"start":{"row":5,"column":2},"end":{"row":5,"column":3},"action":"insert","lines":["a"]},{"start":{"row":5,"column":3},"end":{"row":5,"column":4},"action":"insert","lines":["t"]}],[{"start":{"row":5,"column":3},"end":{"row":5,"column":4},"action":"remove","lines":["t"],"id":20},{"start":{"row":5,"column":2},"end":{"row":5,"column":3},"action":"remove","lines":["a"]},{"start":{"row":5,"column":1},"end":{"row":5,"column":2},"action":"remove","lines":["D"]}],[{"start":{"row":5,"column":1},"end":{"row":5,"column":2},"action":"insert","lines":["d"],"id":21},{"start":{"row":5,"column":2},"end":{"row":5,"column":3},"action":"insert","lines":["a"]}],[{"start":{"row":5,"column":1},"end":{"row":5,"column":3},"action":"remove","lines":["da"],"id":22},{"start":{"row":5,"column":1},"end":{"row":5,"column":10},"action":"insert","lines":["dataclass"]}],[{"start":{"row":6,"column":15},"end":{"row":7,"column":53},"action":"remove","lines":["","    def __init__(self, val=0, left=None, right=None):"],"id":23}],[{"start":{"row":7,"column":8},"end":{"row":7,"column":13},"action":"remove","lines":["self."],"id":24}],[{"start":{"row":8,"column":8},"end":{"row":8,"column":14},"action":"remove","lines":["self.l"],"id":25}],[{"start":{"row":9,"column":8},"end":{"row":9,"column":13},"action":"remove","lines":["self."],"id":26}],[{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"insert","lines":["l"],"id":27}],[{"start":{"row":12,"column":34},"end":{"row":12,"column":38},"action":"remove","lines":["root"],"id":28},{"start":{"row":12,"column":33},"end":{"row":12,"column":34},"action":"remove","lines":[" "]}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":1},"action":"insert","lines":["i"],"id":29},{"start":{"row":4,"column":1},"end":{"row":4,"column":2},"action":"insert","lines":["m"]},{"start":{"row":4,"column":2},"end":{"row":4,"column":3},"action":"insert","lines":["p"]},{"start":{"row":4,"column":3},"end":{"row":4,"column":4},"action":"insert","lines":["o"]},{"start":{"row":4,"column":4},"end":{"row":4,"column":5},"action":"insert","lines":["r"]},{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":4,"column":6},"end":{"row":4,"column":7},"action":"insert","lines":[" "],"id":30},{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"insert","lines":["m"]},{"start":{"row":4,"column":8},"end":{"row":4,"column":9},"action":"insert","lines":["a"]},{"start":{"row":4,"column":9},"end":{"row":4,"column":10},"action":"insert","lines":["t"]},{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"insert","lines":["h"]}],[{"start":{"row":4,"column":11},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":31}],[{"start":{"row":7,"column":15},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":34},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "]},{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"insert","lines":["f"]},{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"insert","lines":["e"]},{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"insert","lines":["g"]}],[{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"remove","lines":["g"],"id":35},{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"remove","lines":["e"]},{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"remove","lines":["f"]}],[{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"insert","lines":["d"],"id":36},{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"insert","lines":["e"]},{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"insert","lines":["f"]}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":23},"action":"remove","lines":["Your module description"],"id":37},{"start":{"row":1,"column":0},"end":{"row":1,"column":67},"action":"insert","lines":["https://leetcode.com/problems/validate-binary-search-tree/solution/"]}],[{"start":{"row":1,"column":67},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":38}],[{"start":{"row":4,"column":0},"end":{"row":29,"column":29},"action":"remove","lines":["from dataclasses import dataclass","import math","","@dataclass","class TreeNode:","    def","        val = x","        left = None","        right = None","        ","class Solution:","    def isValidBST(self, TreeNode):","        ","        def validate(node, low=-math.inf, high=math.inf):","            # Empty trees are valid BSTs.","            if not node:","                return True","            # The current node's value must be between low and high.","            if node.val <= low or node.val >= high:","                return False","            ","            # The left and right subtree must also be valid.","            return (validate(node.right, node.val, high) and","                   validate(node.left, low, node.val))","        ","        return validate(root)"],"id":39},{"start":{"row":4,"column":0},"end":{"row":27,"column":8},"action":"insert","lines":["# Definition for a binary tree node.","# class TreeNode:","#     def __init__(self, val=0, left=None, right=None):","#         self.val = val","#         self.left = left","#         self.right = right","","class Solution:","    def isValidBST(self, root: TreeNode) -> bool:","        ","        def validate(node, low=-math.inf, high=math.inf):","            # Empty trees are valid BSTs.","            if not node:","                return True","            # The current node's value must be between low and high.","            if node.val <= low or node.val >= high:","                return False","            ","            # The left and right subtree must also be valid.","            return (validate(node.right, node.val, high) and","                   validate(node.left, low, node.val))","        ","        return validate(root)","        "]}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":2},"action":"remove","lines":["# "],"id":40},{"start":{"row":6,"column":0},"end":{"row":6,"column":2},"action":"remove","lines":["# "]},{"start":{"row":7,"column":0},"end":{"row":7,"column":2},"action":"remove","lines":["# "]},{"start":{"row":8,"column":0},"end":{"row":8,"column":2},"action":"remove","lines":["# "]},{"start":{"row":9,"column":0},"end":{"row":9,"column":2},"action":"remove","lines":["# "]}],[{"start":{"row":12,"column":40},"end":{"row":12,"column":49},"action":"remove","lines":[" -> bool:"],"id":41}],[{"start":{"row":12,"column":29},"end":{"row":12,"column":39},"action":"remove","lines":[": TreeNode"],"id":42}],[{"start":{"row":12,"column":30},"end":{"row":12,"column":31},"action":"insert","lines":[":"],"id":43}],[{"start":{"row":3,"column":3},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":44},{"start":{"row":4,"column":0},"end":{"row":4,"column":1},"action":"insert","lines":["i"]},{"start":{"row":4,"column":1},"end":{"row":4,"column":2},"action":"insert","lines":["m"]},{"start":{"row":4,"column":2},"end":{"row":4,"column":3},"action":"insert","lines":["p"]},{"start":{"row":4,"column":3},"end":{"row":4,"column":4},"action":"insert","lines":["o"]},{"start":{"row":4,"column":4},"end":{"row":4,"column":5},"action":"insert","lines":["r"]},{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":4,"column":6},"end":{"row":4,"column":7},"action":"insert","lines":[" "],"id":45},{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"insert","lines":["m"]},{"start":{"row":4,"column":8},"end":{"row":4,"column":9},"action":"insert","lines":["a"]},{"start":{"row":4,"column":9},"end":{"row":4,"column":10},"action":"insert","lines":["t"]},{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"insert","lines":["h"]}],[{"start":{"row":4,"column":11},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":46}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":17,"column":25},"end":{"row":17,"column":25},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1608847058219,"hash":"c781a97ac93b411942037baf02aeb94d4c637543"}