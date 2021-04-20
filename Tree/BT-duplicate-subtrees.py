"""
https://leetcode.com/problems/find-duplicate-subtrees/
https://leetcode.com/problems/find-duplicate-subtrees/solution/
"""


# A node structure
class Node:

	# A utility function to create a new node
	def __init__(self, key):
		self.data = key 
		self.left = None
		self.right = None


from collections import Counter

def findDuplicateSubtrees(root):
    ans = []
    count = Counter()
    
    def helper(node):
        if not node:    return '#'
        serial="{},{},{}".format(node.data, helper(node.left), helper(node.right))
        print(serial)
        count[serial]+=1
        if count[serial] == 2:
            ans.append(node.data)
        return serial
    
    helper(root)
    return ans
        
'''
for left node
serial='5,#,#'
count[serial]+=1

for right node
serial='5,#,#'
count[serial]+=1; this is now 2
'''



from collections import defaultdict

def findDuplicateSubtreesEfficient(root):
    ans = []
    count = Counter()
    trees = defaultdict()
    trees.default_factory = trees.__len__
    
    def helper(node):
        if node:
            uid = trees[node.data, helper(node.left), helper(node.right)]
            count[uid]+=1
            if count[uid]==2:
                ans.append(node.data)
            return uid
    
    helper(root)
    return ans


# Driver program to test above function
root = Node(2)
root.left = Node(5)
root.right = Node(5)

print(findDuplicateSubtrees(root))
# print(findDuplicateSubtreesEfficient(root))