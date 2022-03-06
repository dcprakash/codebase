# https://leetcode.com/problems/leftmost-column-with-at-least-a-one/solution/
# A row-sorted binary matrix as input is given, we can also use binary search
# binary search in matrix

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
    lefft_most=cols
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
            lefft_most=min(lefft_most,lo)
            
    return -1 if lefft_most==cols else lefft_most



binaryMatrix=[[0,0],
              [1,1]]
# print(leftMostColumnWithOne(binaryMatrix))
print(leftMostColumnWithOneEfficient(binaryMatrix))


'''
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        smallest_index = cols
        for row in range(rows):
            # Binary Search for the first 1 in the row.
            lo = 0
            hi = cols - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if binaryMatrix.get(row, mid) == 0:
                    lo = mid + 1
                else:
                    hi = mid
            # If the last element in the search space is a 1, then this row
            # contained a 1.
            if binaryMatrix.get(row, lo) == 1:
                smallest_index = min(smallest_index, lo)
        # If smallest_index is still set to cols, then there were no 1's in 
        # the grid. 
        return -1 if smallest_index == cols else smallest_index
'''