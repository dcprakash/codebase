# https://leetcode.com/problems/course-schedule-ii/solution/
# Dijkstra, Topological sort, courses, prerequisites, schedule, dependency, adjacency list
# dfs depth first search

from collections import defaultdict
class Solution:

    WHITE = 1   #not visited
    GRAY = 2    #inprogress
    BLACK = 3   #visited, no more route to new vertex

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        # Create the adjacency list representation of the graph
        adj_list = defaultdict(list)    # {0: [1, 2], 1: [3], 2: [3]}   to take 1 and 2, we need 0

        # A pair [a, b] in the input represents edge from b --> a
        for dest, src in prerequisites:
            adj_list[src].append(dest)

        topological_sorted_order = []
        is_possible = True

        # By default all vertces are WHITE
        color = {k: Solution.WHITE for k in range(numCourses)}
        def dfs(node):
            nonlocal is_possible

            # Don't recurse further if we found a cycle already
            if not is_possible:
                return

            # Start the recursion
            color[node] = Solution.GRAY

            # Traverse on neighboring vertices
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == Solution.WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == Solution.GRAY:
                         # An edge to a GRAY vertex represents a cycle
                        is_possible = False

            # Recursion ends. We mark it as black
            color[node] = Solution.BLACK
            topological_sorted_order.append(node)

        for vertex in range(numCourses):
            # If the node is unprocessed, then call dfs on it.
            if color[vertex] == Solution.WHITE:
                dfs(vertex)

        return topological_sorted_order[::-1] if is_possible else []



numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
s=Solution()
print(s.findOrder(numCourses, prerequisites))


'''
We can represent the information provided in the question in the form of a graph.
Let G(V, E)G(V,E) represent a directed, unweighted graph.
Each course would represent a vertex in the graph.
'''