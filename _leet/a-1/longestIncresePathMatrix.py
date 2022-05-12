# https://www.geeksforgeeks.org/longest-increasing-path-matrix/
# https://leetcode.com/explore/interview/card/google/61/trees-and-graphs/3072/


def longestIncreasingPath(matrix):
    
    def dfs(i, j):
        count = 1
        for d in dirs:
            x = i + d[0]
            y = j + d[1]
            if x>=0 and x<m and y>=0 and y<n and matrix[x][y]>matrix[i][j]:
                count=max(count, 1+dfs(x,y))
        return count
    
    def dfs_cache(i, j):
        if (i,j) in cache:
            return cache[(i,j)]
        count = 1
        for d in dirs:
            x = i + d[0]
            y = j + d[1]
            if x>=0 and x<m and y>=0 and y<n and matrix[x][y]>matrix[i][j]:
                count = max(count, 1+dfs_cache(x,y))
        cache[(i,j)] = count
        return count
    
    dirs = [[0,1],[1,0],[0,-1],[-1,0]]
    if len(matrix)==0: return 0
    m=len(matrix)
    n=len(matrix[0])
    ans=0
    cache = {}
    for i in range(m):
        for j in range(n):
            # ans=max(ans, dfs(i, j))
            ans=max(ans, dfs_cache(i, j))
    return ans
    

matrix = [[1, 2],
          [3, 4]]
print(longestIncreasingPath(matrix))