'''
https://leetcode.com/problems/pascals-triangle

pascal triangle
'''

class Solution:
    def generate(self, numRows):
        triangle = []
        
        for row_ix in range(numRows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_ix+1)]
            row[0], row[-1] = 1, 1 
        
            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row)-1):
                row[j] = triangle[row_ix-1][j-1] + triangle[row_ix-1][j]
            
            triangle.append(row)

        return triangle
        
obj=Solution()
# print(obj.countBinarySubstrings("10101"))
print(obj.generate(4))
