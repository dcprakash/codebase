'''
https://leetcode.com/problems/monotonic-array
    
'''

class Solution:
    def isMonotonic(self, nums):
        inc = dec = True
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                inc=False
            if nums[i]<nums[i+1]:
                dec=False
        # print(inc, dec)
        return inc or dec
        
        
obj=Solution()
print(obj.isMonotonic([1,2,2,3]))
# print(obj.isMonotonic([6,5,4,4]))
# print(obj.isMonotonic([1,2,2,3,1]))

