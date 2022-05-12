"""
https://leetcode.com/explore/interview/card/facebook/55/dynamic-programming-3/3037/
"""

class NumMatrix:

    def __init__(self, matrix):
        self.matrix = matrix
        

    def sumRegion(self, row1, col1, row2, col2):
        i=len(self.matrix)
        j=len(self.matrix[0])
        # print(i,j)    

        res=0

        for m in range(row1,row2+1):
            for n in range(col1,col2+1):
                # print(self.matrix[m][n])
                res+=self.matrix[m][n]
        return res


matrix=[
          [3, 0, 1, 4],
          [5, 6, 3, 2],
          [1, 2, 0, 1],
          [4, 1, 0, 1],
          [1, 0, 3, 0]
        ]
row1,col1=2,1
row2,col2=3,2
obj = NumMatrix(matrix)
print(obj.sumRegion(row1,col1,row2,col2))


