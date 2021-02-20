'''
https://leetcode.com/problems/minimum-path-sum/solution/

minimum path sum in matrix
maximum path sum in matrix
'''
# https://leetcode.com/problems/minimum-path-sum/
import sys

def minPathSum(grid, i, j):
    if i==len(grid) or j==len(grid[0]):    return float("inf")
    if i==len(grid)-1 and j==len(grid[0])-1:    return grid[i][j]
    return grid[i][j] + min(minPathSum(grid,i+1,j), minPathSum(grid,i,j+1))
    

def minPathSumEfficient(grid, i, j):
    dp = [[None for j in range(len(grid))] for i in range(len(grid[0]))]
    for i in range(len(grid)-1, -1, -1):
        for j in range(len(grid[0])-1,-1,-1):
            if i==len(grid)-1 and j!=len(grid[0])-1:
                dp[i][j]=grid[i][j]+dp[i][j+1]
            elif i!=len(grid)-1 and j==len(grid[0])-1:
                dp[i][j]=grid[i][j]+dp[i+1][j]
            elif i!=len(grid)-1 and j!=len(grid[0])-1:
                dp[i][j]=grid[i][j]+min(dp[i+1][j],dp[i][j+1])
            else:
                dp[i][j]=grid[i][j]
    return dp[0][0]
    

grid = [[1,3,1],
        [1,5,1],
        [4,2,1]]
# print(minPathSum(grid, 0, 0))
print(minPathSumEfficient(grid, 0, 0))

