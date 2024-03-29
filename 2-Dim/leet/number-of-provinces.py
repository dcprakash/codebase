# Program to count islands in boolean 2D matrix
# https://www.geeksforgeeks.org/find-number-of-islands/
# https://leetcode.com/problems/number-of-provinces/solution/
# same as find-islands but, we are not looking for 4 directional neighbors; instead we look for below
'''
  0 1 2 3
0[1,0,0,1]
1[0,1,1,0]
2[0,1,1,1]
3[1,0,1,1]

  0--3
     |
  1--2
  
  
  0 1 2 3
0[1,0,0,1]
1[0,1,0,0]
2[0,0,1,1]
3[1,0,1,1]

  0--3
     |
  1  2
'''

class Solution:
    def dfs(self,row,graph,visited):
        visited.append(row)
        for col in range(len(graph)):
            if graph[row][col]==1 and col not in visited:
                self.dfs(col,graph,visited)
    
    def findCircleNum(self,graph):
        visited=[]
        count=0
        for row in range(len(graph)):
            if row not in visited:
                self.dfs(row,graph,visited)
                count+=1
        return count


# graph=[[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
grid=[[1,0,0,1],[0,1,0,0],[0,0,1,1],[1,0,1,1]]
s=Solution()
print(s.findCircleNum(grid))



'''
below is simple example of find islands

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
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
'''