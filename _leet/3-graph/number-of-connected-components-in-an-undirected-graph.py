"""
number-of-connected-components-in-an-undirected-graph
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

DFS
undirected graph

"""
from collections import defaultdict

class Solution:
    def countComponents(self, n, edges):
        
        def construct_graph():
            for edge in edges:
                src, dest = edge
                graph[src].append(dest)
                graph[dest].append(src)
        
        
        def dfs(node, visited):
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor]=True
                    dfs(neighbor, visited)
            
        
        if not edges:   return n
        
        graph=defaultdict(list)
        construct_graph()
        count=0
        visited=[False]*n
        
        for node in range(n):
            if not visited[node]:
                count+=1
                visited[node]=True
                dfs(node, visited)
        
        return count    


n = 5
edges = [[0, 1], [1, 2], [3, 4]]
s=Solution()
print(s.countComponents(n, edges))
