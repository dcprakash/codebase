"""
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""


def findItemInCicularSortedArray(nums, target):
    low=0
    high=len(nums)-1
    
    while low<=high:
        mid=(low+high)//2;
        if target==nums[mid]:
            return mid
        if nums[mid]<=nums[high]:
            if target>=nums[mid] and target<=nums[high]:
                low=mid+1
            else:
                high=mid-1
        else:
            if target<=nums[mid] and target>=nums[low]:
                high=mid-1
            else:
                low=mid+1
    return -1    

nums = [1,3]
target = 3

print(findItemInCicularSortedArray(nums,target))
