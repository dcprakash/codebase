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
    

grid = [[1,3,1],
        [1,5,1],
        [4,2,1]]
print(minPathSum(grid, 0, 0))
# print(minPathSumEfficient(grid, 0, 0))

'''
  public int minPathSum(int[][] grid) {
        int[][] dp = new int[grid.length][grid[0].length];
        for (int i = grid.length - 1; i >= 0; i--) {
            for (int j = grid[0].length - 1; j >= 0; j--) {
                if(i == grid.length - 1 && j != grid[0].length - 1)
                    dp[i][j] = grid[i][j] +  dp[i][j + 1];
                else if(j == grid[0].length - 1 && i != grid.length - 1)
                    dp[i][j] = grid[i][j] + dp[i + 1][j];
                else if(j != grid[0].length - 1 && i != grid.length - 1)
                    dp[i][j] = grid[i][j] + Math.min(dp[i + 1][j], dp[i][j + 1]);
                else
                    dp[i][j] = grid[i][j];
            }
        }
        return dp[0][0];
    }
'''
