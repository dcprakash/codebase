'''
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

sort given array
compare orginal and sorted array
determine the leftmost and righmost mismatch
subarray lying inbetween need to be sorted
      0. 1. 2.  3. 4. 
orig=[2, 6, 10, 9, 15]
sort=[2, 6, 9, 10, 15]
subarry b.w 2 and 3 need to be sorted
'''

class Solution:
    def findUnsortedSubarray(self, nums):
        if len(nums)==1: return 0
        sort_nums=nums[:]
        sort_nums.sort()
        start=len(nums)-1
        end=0
        for i in range(len(nums)):
            if sort_nums[i] != nums[i]:
                start=min(start, i) #to get left most unsorted index
                end=max(end, i)  #to get right most unsorted index
        return end-start+1 if end-start>=0 else 0   #return 0 for already sorted array

# nums = [1,2,3,4]
# nums = [2,6,10,9,15]
# nums = [2,6,4,8,10,9,15]
nums = [2,1]
s=Solution()
print(s.findUnsortedSubarray(nums))


