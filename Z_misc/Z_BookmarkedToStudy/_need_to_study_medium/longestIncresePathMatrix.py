# https://www.geeksforgeeks.org/longest-increasing-path-matrix/
# https://leetcode.com/explore/interview/card/google/61/trees-and-graphs/3072/

import math

dirs = [[0,1],[1,0],[0,-1],[-1,0]]

def dfs(matrix, i, j, cache):
    m=len(matrix)
    n=len(matrix[0])
    if cache[i][j]!=0: return cache[i][j]
    for d in dirs:
        x = i + d[0]
        y = j + d[1]
        if x>=0 and x<m and y>=0 and y<n and matrix[x][y]>matrix[i][j]:
            cache[i][j]=max(cache[i][j], dfs(matrix,x,y,cache))
    return cache[i][j] + 1


def longestIncreasingPath(matrix):
    if len(matrix)==0: return 0
    m=len(matrix)
    n=len(matrix[0])
    ans=0
    cache = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            ans=max(ans, dfs(matrix, i, j, cache))
    return ans
    

matrix = [[1, 2],
       [3, 4]]
print(longestIncreasingPath(matrix))