


def isSafe(i,j,visited):
    ret_value = (i>=0 and i<=row and j>=0 and j<=col and graph[i][j] and not visited[i][j])
    return ret_value

def DFS(i,j,visited):
    row=[-1,-1,-1,0,0,1,1,1]
    col=[-1,0,1,-1,1,-1,0,1]
    visited[i][j]=True
    for k in range(8):
        if isSafe(i+row[k],j+col[k],visited):
            DFS(i+row[k],j+col[k],visited)



def countIslands(row,col,graph):
    visited=[False for j in range(col) for i in range(row)]
    count = 0
    for i in range(row):
        for j in range(col):
            if graph[i][j] and visited[i][j]==False:
                DFS(i,j,visited)
                count+=1
    return count
            