"""
https://leetcode.com/problems/merge-sorted-array

The simplest implementation would be to make a copy of the values in nums1, called nums1Copy, 
    and then use two read pointers and one write pointer to read values from nums1Copy and nums2 and write them into nums1.

Initialize nums1Copy to be a new array containing the first m values of nums1.
Initialize read pointer p1 to the beginning of nums1Copy.
Initialize read pointer p2 to the beginning of nums2.
Initialize write pointer p to the beginning of nums1.
While p is still within nums1:
    If nums1Copy[p1] exists and is less than or equal to nums2[p2]:
        Write nums1Copy[p1] into nums1[p], and increment p1 by 1.
    Else
        Write nums2[p2] into nums1[p], and increment p2 by 1.
Increment p by 1.

"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Do not return anything, modify nums1 in-place instead.

        # Make a copy of the first m elements of nums1.
        nums1_copy = nums1[:m] 
        
        # Read pointers for nums1Copy and nums2 respectively.
        p1 = 0
        p2 = 0
        
        # Compare elements from nums1Copy and nums2 and write the smallest to nums1.
        for p in range(n + m):
            # We also need to ensure that p1 and p2 aren't over the boundaries
            # of their respective arrays.
            # p2 can be bigger than n, bcz m is big and also due to n+m
            if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
                nums1[p] = nums1_copy[p1] 
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
nums1=sorted(nums1[:m]+nums2[:n])
print(nums1[:])
# print(sorted(nums1[:m]+nums2[:n]))

