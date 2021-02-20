# https://leetcode.com/problems/search-a-2d-matrix-ii/submissions/
# binart search in matrix

def searchMatrix(matrix,target):
    rows = len(matrix)
    cols = len(matrix[0])
    l=cols
    for row in range(rows):
        lo=0
        hi=cols-1
        while lo<=hi:
            mid=(lo+hi)//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]<target:
                lo+=1   #why not lo=mid+1?
            else:
                hi-=1
    return False
    

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(searchMatrix(matrix,target))