'''
https://leetcode.com/problems/spiral-matrix/
print matrix in sprial order
'''

class Solution:
    def spiralOrder(self, matrix):
        res=[]
        top=0
        bottom=len(matrix)-1
        left=0
        right=len(matrix[0])-1
        dir=0
        
        while top<=bottom and left<=right:
            if dir==0:
                for m in range(left,right+1):
                    res.append(matrix[top][m])
                top+=1
                dir=(dir+1)%4
            elif dir==1:
                for m in range(top,bottom+1):
                    res.append(matrix[m][right])
                right-=1
                dir=(dir+1)%4
            elif dir==2:
                for m in range(right,left-1,-1):
                    res.append(matrix[bottom][m])
                bottom-=1
                dir=(dir+1)%4
            elif dir==3:
                for m in range(bottom,top-1,-1):
                    res.append(matrix[m][left])
                left+=1
                dir=(dir+1)%4

        return res


matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
s=Solution()
print(s.spiralOrder(matrix))
