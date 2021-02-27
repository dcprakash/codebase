
def sumt(root):
    if not root:    return 0
    return sumt(root.left) + root.data + sumt(root.right)

def sumTree(root):
    if not root or (root.left == root.right == None):
        return 1
    ls=sumt(root.left)
    rs=sumt(root.right)
    if ls+rs==root.data and sumTree(root.left) and sumTree(root.right):
        return 1