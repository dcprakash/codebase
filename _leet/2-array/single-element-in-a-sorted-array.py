'''
https://leetcode.com/problems/single-element-in-a-sorted-array/

single element in sorted array
non duplicate element

Starting with the first element, we iterate over every 2nd element, 
    checking whether or not the next element is the same as the current. 
    If it's not, then we know this must be the single element.
if we reach last element, we know the last element is non duplicate, return it
'''


class Solution:
    def singleNonDuplicate(self, nums):
        for i in range(0, len(nums)-2, 2):
            if nums[i]!=nums[i+1]:
                return nums[i]
        return nums[-1]


nums = [1,1,2,2,3,3,4,4,8]
s=Solution()
print(s.singleNonDuplicate(nums))