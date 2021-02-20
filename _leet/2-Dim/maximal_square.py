'''
https://leetcode.com/problems/maximal-square/
https://www.youtube.com/watch?v=6X7Ha2PrDmM&feature=emb_logo&ab_channel=NeetCode

# dynamic programing
# memoization

largest square, not rectangle
'''


def maximalSquare(matrix):
    row=len(matrix)
    col=len(matrix[0])
    cache={} #dictionary of tuples with location of matrix as key and value as max square
    
    
    def helper(r,c):
        if r>=row or c>=col:
            return 0
        
        if (r,c) not in cache:
            right=helper(r,c+1)
            down=helper(r+1,c)
            diag=helper(r+1,c+1)
            
            cache[(r,c)]=0
            if matrix[r][c]=="1":
                cache[(r,c)]=1+min(right,down,diag)
                
        return cache[(r,c)]
    
    
    helper(0,0)
    print(cache)
    # {(1, 2): 2, (0, 1): 0, (3, 2): 0, (1, 3): 2, (3, 1): 0, (3, 3): 1, (3, 0): 1, (2, 2): 1, (1, 1): 0, (1, 4): 1, (0, 2): 1, (2, 0): 1, (0, 0): 1, (2, 3): 1, (2, 1): 1, (0, 4): 0, (1, 0): 1, (0, 3): 0, (3, 4): 0, (2, 4): 1}
    return max(cache.values()) ** 2
            

# matrix = [
#     ["1","0","1","0","0"],
#     ["1","0","1","1","1"],
#     ["1","1","1","1","1"],
#     ["1","0","0","1","0"]]

matrix = [
    ["1","1"],
    ["1","1"]
    ]
# {(1, 1): 1, (0, 1): 1, (1, 0): 1, (0, 0): 2}    
print(maximalSquare(matrix))
