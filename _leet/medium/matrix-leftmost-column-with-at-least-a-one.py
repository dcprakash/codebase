# https://leetcode.com/problems/leftmost-column-with-at-least-a-one/solution/
# A row-sorted binary matrix as input is given, we can also use binary search


def leftMostColumnWithOne(binaryMatrix):
    rows = len(binaryMatrix)
    cols = len(binaryMatrix[0])
    l=cols
    for row in range(rows):
        for col in range(cols):
            if binaryMatrix[row][col]==1:
                l=min(l,col)
    return -1 if l==cols else l


def leftMostColumnWithOneEfficient(binaryMatrix):
    rows = len(binaryMatrix)
    cols = len(binaryMatrix[0])
    l=cols
    for row in range(rows):
        lo=0
        hi=cols-1
        while lo<hi:
            mid=(lo+hi)//2
            # find left most 1
            if binaryMatrix[row][mid]==0:
                lo=mid+1
            else:
                hi=mid
        
        # if 1 is found in this row
        if binaryMatrix[row][lo]==1:
            l=min(l,lo)
            
    return -1 if l==cols else l



binaryMatrix=[[0,0],
              [1,1]]
# print(leftMostColumnWithOne(binaryMatrix))
print(leftMostColumnWithOneEfficient(binaryMatrix))
