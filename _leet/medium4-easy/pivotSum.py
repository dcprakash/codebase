"""
https://leetcode.com/problems/find-pivot-index/
leftsum == rightsum
left sum equal to right sum
"""
class Solution:
    def pivotIndex(self, nums):
        total=sum(nums)
        leftsum=0
        for i, x in enumerate(nums):
            if leftsum==(total-x-leftsum):
                return i
            leftsum+=x
        return -1
            

obj=Solution()
print(obj.pivotIndex([1,7,3,6,5,6]))