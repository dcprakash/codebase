# https://leetcode.com/problems/matrix-block-sum/
# matrix block sum


def matrixBlockSum(mat, K):
    # Create a cumulative sum matrix where dp[i][j] is the sum of all cells in 
    # the rectangle from (0,0) to (i,j),
    dp = [[0]*(len(mat[0])+1) for _ in range(len(mat)+1)]
    for i in range(1,len(mat)+1): #dp[i][j] record the sum mat[x][y](0<=x<=i-1, 0<=y<=j-1)
        for j in range(1,len(mat[0])+1):
            # - dp[i-1][j-1] bcz its already part of dp[i-1][j] & dp[i][j-1]
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + mat[i-1][j-1]
    ans = mat.copy()

    for i in range(len(mat)): 
        for j in range(len(mat[0])):
            upleft_x, upleft_y = max(0,i-K), max(0,j-K)
            downright_x, downright_y = min(len(mat),i+K+1), min(len(mat[0]),j+K+1)
            downleft_x, downleft_y = downright_x, upleft_y
            upright_x, upright_y = upleft_x, downright_y
            print(dp[downright_x][downright_y],dp[downleft_x][downleft_y],dp[upright_x][upright_y],dp[upleft_x][upleft_y])
            ans[i][j] = dp[downright_x][downright_y] - dp[downleft_x][downleft_y] - dp[upright_x][upright_y] + dp[upleft_x][upleft_y]
    return ans


mat = [[1,2,3],[4,5,6],[7,8,9]]
K = 1
print(matrixBlockSum(mat,K))


'''
[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

[
     [0, 0, 0, 0], 
     [0, 1, 3, 6], 
     [0, 5, 12, 21], 
     [0, 12, 27, 45]
]

[
    [12,21,16],
    [27,45,33],
    [24,39,28]
]



'''