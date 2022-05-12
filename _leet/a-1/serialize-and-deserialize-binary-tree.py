'''
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
'''
'''
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return str(root.val) + ',' + self.serialize(root.left) + self.serialize(root.right) if root else 'None,'
#         def rserialize(root, string):
#             """ a recursive helper function for the serialize() function."""
#             # check base case
#             if root is None:
#                 string += 'None,'
#             else:
#                 string += str(root.val) + ','
#                 string = rserialize(root.left, string)
#                 string = rserialize(root.right, string)
#             return string
#         res=rserialize(root, '')
#         print(res)
#         return res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(data)
        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            if l[0] == 'None':
                l.pop(0)
                return None
                
            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))