"""
https://leetcode.com/problems/design-file-system/solution/

The basic data structure that is used for representing a Trie is a dictionary. 
    The dictionary and other potential flags/data values can be a part of a custom TreeNode data structure. 
    For this problem, we will have a TrieNode data structure that will contain three things 
        1. The string representing the path name. 
        2. The value corresponding to this path. 
        3. And finally, a dictionary representing the outgoing connections to other TrieNodes.

The root of our trie will be a TrieNode containing the empty string.

Create()
    First, we will split the given path into various components using / as the delimiter. 
    So for the path /a/b/c, we will have four components namely , a, b, and c.

"""
from collections import defaultdict

class TrieNode(object):
    def __init__(self, name):        
        self.name = name
        self.value = -1
        self.map = defaultdict(TrieNode)
        
class FileSystem:

    def __init__(self):
        
        # Root node contains the empty string.
        self.root = TrieNode("")

    def createPath(self, path: str, value: int) -> bool:
        
        # Obtain all the components
        components = path.split("/")
        
        # Start "curr" from the root node.
        cur = self.root
        
        # Iterate over all the components.
        for i in range(1, len(components)):
            name = components[i]
            
            # For each component, we check if it exists in the current node's dictionary.
            if name not in cur.map:
                
                # If it doesn't and it is the last node, add it to the Trie.
                if i == len(components) - 1:
                    cur.map[name] = TrieNode(name)
                else:
                    # If /a/b/c is path, and this is first createPath call; if we did not
                    # create parent directories a and b, we cannot create c and hence, return False
                    return False
            cur = cur.map[name]
        
        # Value not equal to -1 means the path already exists in the trie. 
        if cur.value!=-1:
            return False
        
        cur.value = value
        return True

    def get(self, path: str) -> int:
        
        # Obtain all the components
        print(self.root)
        cur = self.root
        
        # Start "curr" from the root node.
        components = path.split("/")
        
        # Iterate over all the components.
        for i in range(1, len(components)):
            
            # For each component, we check if it exists in the current node's dictionary.
            name = components[i]
            if name not in cur.map:
                return -1
            cur = cur.map[name]
        return cur.value


f=FileSystem()
f.createPath("/leet",1)
f.createPath("/leet/code",2)
print(f.get("/leet/code"))
f.createPath("/leet",1)
print(f.get("/c"))

