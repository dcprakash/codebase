# Program to count islands in boolean 2D matrix
# https://www.geeksforgeeks.org/find-number-of-islands/
# same as number-of-provinces


class Solution:
    def findCircleNum(self, isConnected):
        
        def dfs(i,j):
            seen.add((i,j))
            for d in directions:
                newi=i+d[0]
                newj=j+d[1]
                if 0<=newi<m and 0<=newj<n and isConnected[i][j]==1 and (newi, newj) not in seen:
                    dfs(newi, newj)
            
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        seen=set()
        m=len(isConnected)
        n=len(isConnected[0])
        count=0
        for i in range(m):
            for j in range(n):
                if isConnected[i][j]==1 and (i, j) not in seen:
                    dfs(i,j)
                    count+=1
        return count


# graph = [[1,0,0],[0,1,0],[0,0,1]]

# graph = [[1, 1, 0, 0, 0],
#          [0, 1, 0, 0, 1],
#          [1, 0, 0, 1, 1],
#          [0, 0, 0, 0, 0],
#          [1, 0, 1, 0, 1]]
         
# row = len(graph)
# col = len(graph[0])
# g = Graph(row, col, graph)
# print("Number of islands is:")
# print(g.countIslands())

graph= [[1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,0,1,1],
        [0,0,0,1,1]]
s=Solution()
print(s.findCircleNum(graph))

'''
class Graph:
    def __init__(self, row, col, g):
        self.ROW = row
        self.COL = col
        self.graph = g

    # A function to check if a given cell
    # (row, col) can be included in DFS
    def isSafe(self, i, j, visited):
        # row number is in range, column number
        # is in range and value is 1
        # and not yet visited
        ret_value = (i >= 0 and i < self.ROW and
                j >= 0 and j < self.COL and
                not visited[i][j] and self.graph[i][j])
        #print "for i {}, j {}, visited[i][j], self.graph[i][j], its {}".format(i, j, visited[i][j], self.graph[i][j], ret_value)
        return ret_value

    # A utility function to do DFS for a 2D
    # boolean matrix. It only considers
    # the 8 neighbours as adjacent vertices
    def DFS(self, i, j, visited):

        # These arrays are used to get row and
        # column numbers of 8 neighbours
        # of a given cell directions / path
        rowNbr = [-1, 0, 0, 1];
        colNbr = [0, -1, 1, 0];
        # rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1];
        # colNbr = [-1, 0, 1, -1, 1, -1, 0, 1];
        # -1,-1   -1,0    -1,1
        # 0,-1    ****    0,1
        # 1,-1    1,0     1,1
        
        # Mark this cell as visited
        visited[i][j] = True
        # print("Checking for i {}, j {} : {}".format(i, j, visited[i][j]))
        # Recur for all connected neighbours
        # check if neighbours has 1, then call DFS on them
        for k in range(4):
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
                self.DFS(i + rowNbr[k], j + colNbr[k], visited)


    # The main function that returns
    # count of islands in a given boolean
    # 2D matrix
    def countIslands(self):
        # Make a bool array to mark visited cells.
        # Initially all cells are unvisited
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]
        # print(visited)

        # Initialize count as 0 and travese
        # through the all cells of
        # given matrix
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                # If a cell with value 1 is not visited yet,
                # then new island found
                if visited[i][j] == False and self.graph[i][j] == 1:
                    # Visit all cells in this island
                    # and increment island count
                    self.DFS(i, j, visited)
                    count += 1

        return count
'''