'''
https://leetcode.com/problems/binary-search-tree-iterator/

BST: all elements to left of tree is smaller, and right is larger

1. when next is called, return the "next" smallest number in the tree
    and if next smallest element has right node, add that and its samllest to stack
    stack is used to keep track of smaller elements
2. if stack is not empty, then has_next will return true.

For a given node root, the next smallest element will always be the leftmost element in its tree.
So, for a given root node, we keep on following the leftmost branch until we reach a node which 
doesn't have a left child and that will be the next smallest element.
Rest of the nodes are added to the stack because they are pending processing. 

def inorder_left(root):
   while (root):
     S.append(root)
     root = root.left

It's very easy to implement the hasNext() function since all we need to check is if the stack is empty or not. 
Suppose we get a call to the next() function, we can return top of stack but, will be left with 2 choices:
1. If top of stack is a leaf node, then just pop it
2. Second is where the node has a right child. We don't need to check for the left child because 
    of the way we have added nodes onto the stack

Again, it's important to understand that obtaining the next smallest element doesn't take much time. 
However, some time is spent in maintaining the invariant that the stack top will always have the node we are looking for.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        

class BSTIterator:

    def __init__(self, root: TreeNode):
        # Stack for the recursion simulation
        self.stack = []

        # Remember that the algorithm starts with a call to the helper function
        # with the root node as the input
        self._leftmost_inorder(root)


    def _leftmost_inorder(self, root):
        # For a given node, add all the elements in the leftmost branch of the tree
        # under it to the stack.
        while root:
            self.stack.append(root)
            root = root.left
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        # Node at the top of the stack is the next smallest element; because left most element will be on top
        topmost_node = self.stack.pop()

        # no need to check left child, bcz the way we popullate stack
        # Need to maintain the invariant. If the node has a right child
        # helper function for the right child
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
