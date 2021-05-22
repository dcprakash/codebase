'''
https://leetcode.com/problems/minimum-falling-path-sum/
start from last but one element, and calculate with last element


paint house
steps
stairs
dynamic program
    
'''


class Solution:
    def minFallingPathSum(self, matrix):
        
        n = len(matrix)        
        dp = matrix
        
        # for row in reversed(range(n-1)):
        for row in range(n-2,-1,-1):
            for col in range(n):
                if col == 0:
                    dp[row][col] += min(dp[row+1][col], dp[row+1][col+1])
                elif col == n-1:
                    dp[row][col] += min(dp[row+1][col-1], dp[row+1][col])
                else:
                    dp[row][col] += min(dp[row+1][col-1], dp[row+1][col], dp[row+1][col+1])
                          
        return min(dp[0])
        

        
obj=Solution()
print(obj.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
