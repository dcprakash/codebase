# https://www.geeksforgeeks.org/a-boolean-matrix-question/
# if matrix[i][j] is 1 then make all cells of ith row and jth column as 1


def booleanMatrix(mat):
    row=len(mat)
    col=len(mat[0])
    ret_mat=mat[:]
    visited = [[False for j in range(col)] for i in range(row)]
    
    def issafe(i,j,visited):
        return i>=0 and i<row and j>=0 and j<col
    
    def dfs(i, j, visited):
        visited[i][j]=True
        rownum=[0,1]
        colnum=[1,0]
        for k in range(2):
            if issafe(i+rownum[k], j+colnum[k], visited):
                ret_mat[i+rownum[k]][j+colnum[k]]=1
                dfs(i+rownum[k], j+colnum[k], visited)
    
    for i in range(row):
        for j in range(col):
            if mat[i][j]==1 and not visited[i][j]:
                dfs(i, j, visited)
    
    return ret_mat


matrix=[[1,0,1],
        [0,0,0],
        [0,0,0]]
print(booleanMatrix(matrix))