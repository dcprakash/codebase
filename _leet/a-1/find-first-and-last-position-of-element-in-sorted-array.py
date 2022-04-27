'''
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/
similar to Array/count-number-of-occurrences-or-frequency-in-a-sorted-array.py

binary search
left most
right most
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findOcuurence(n, left):
            l=0
            r=n-1
            while l<=r:
                m=(l+r)//2
                if nums[m]==target:
                    if left:
                        if m==l or nums[m-1]<target:    return m
                        r=m-1
                    else:
                        if m==r or nums[m+1]>target:    return m
                        l=m+1
                elif target<nums[m]:
                    r=m-1
                else:
                    l=m+1
            return -1
        
        n=len(nums)
        leftIndex=findOcuurence(n,True)
        rightIndex=findOcuurence(n,False)
        return [leftIndex,rightIndex] if leftIndex!=-1 else [-1,-1]
        