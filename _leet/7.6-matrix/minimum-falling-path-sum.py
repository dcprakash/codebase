'''
https://leetcode.com/problems/minimum-falling-path-sum/
start from last but one element, and calculate with last element

    
'''


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)
        
        # for row in reversed(range(n-1)):
        for row in range(n-2,-1,-1):
            for col in range(n):
                if col == 0:
                    matrix[row][col] += min(matrix[row+1][col], matrix[row+1][col+1])
                elif col == n-1:
                    matrix[row][col] += min(matrix[row+1][col-1], matrix[row+1][col])
                else:
                    matrix[row][col] += min(matrix[row+1][col-1], matrix[row+1][col], matrix[row+1][col+1])
                          
        return min(matrix[0])
        

        
obj=Solution()
print(obj.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
