# https://leetcode.com/problems/find-peak-element/
# peak element in an array or list
# Whenever, we find a number nums[i]nums[i], we only need to check if it is larger than
# the next number nums[i+1]nums[i+1] for determining if nums[i]nums[i] is the peak element
# no need to check nums[i-1]<nums[i]
# if nums[i-1]<nums[i]>nums[i+1]: 


class Solution:
    def findPeakElement(self, nums):
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                return i
        return len(nums)-1  # corner case if list has 1 element
        
        
    def search(self, nums, l, r):
        if l==r:    return l
        mid = (l+r)//2;
        if nums[mid]>nums[mid+1]:   return self.search(nums, l, mid)
        else:   return self.search(nums, mid+1, r)
        
        
    def findPeakElementBinarySearch(self, nums):
        return self.search(nums, 0, len(nums)-1)
        
    #.  0 1 2 3
nums = [1,2,3,1]
s=Solution()
# print(s.findPeakElement(nums))
print(s.findPeakElementBinarySearch(nums))