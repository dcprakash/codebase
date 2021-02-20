# https://leetcode.com/problems/clone-graph/
'''
Each node's value is the same as the node's index (1-indexed). 
For example, the first node with val = 1, the second node with val = 2

DFS
     we don't want to get stuck in a cycle while we are traversing the graph; keep track of visited
     hash map with key as original node and values as cloned node

'''


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):

    def __init__(self):
        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        self.visited = {}

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node
        print(node.val)
        print([n.val for n in node.neighbors])
        # If the node was already visited before.
        # Return the clone from the visited dictionary.
        if node in self.visited:
            return self.visited[node]

        # Create a clone for the given node.
        # Note that we don't have cloned neighbors as of now, hence [].
        clone_node = Node(node.val, [])

        # The key is original node and value being the clone node.
        self.visited[node] = clone_node
        print([n.val for n in self.visited])

        # Iterate through the neighbors to generate their clones
        # and prepare a list of cloned neighbors to be added to the cloned node.
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node
        
        
'''
    1   2       3   4       node    
[[2,4],[1,3],[2,4],[1,3]]   neighbors

'''