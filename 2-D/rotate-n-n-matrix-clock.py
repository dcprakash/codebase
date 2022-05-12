'''
# Python3 program to rotate a matrix by 90 degrees 
# https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/
# https://leetcode.com/problems/rotate-image/submissions/

[1,2,3]
[4,5,6]
[7,8,9]

[7,4,1]
[8,5,2]
[9,6,3]
'''


class Solution:
	def rotate(self, matrix):
		"""
		Do not return anything, modify matrix in-place instead.
		"""
		print(matrix)
		N=len(matrix)
		for x in range(0, int(N / 2)):
			for y in range(x, N-1-x):
				temp = matrix[N-1-y][x]
				matrix[N-1-y][x] = matrix[N-1-x][N-1-y]
				matrix[N-1-x][N-1-y] = matrix[y][N-1-x]
				matrix[y][N-1-x ]=matrix[x][y]
				matrix[x][y] = temp
		print(matrix)

                
s=Solution()
s.rotate([[1,2,3],[4,5,6],[7,8,9]])