'''
https://leetcode.com/problems/maximum-swap/

swap one element to get biggest number

convert int to list
duplicate this list
from left to right:
    swap original array oarr by one element
    if oarr is greater than duplicate narr
        copy sorted array to duplicate narr
'''

class Solution:
    def maximumSwap(self, nums):
        oarr=list(str(nums))
        narr=oarr[:]
        n=len(oarr)
        for i in range(n):
            for j in range(i+1, n):
                oarr[i],oarr[j]=oarr[j],oarr[i]
                if narr<oarr:   narr=oarr[:]
                oarr[i],oarr[j]=oarr[j],oarr[i]
        return "".join(narr)

    # cannot achieve this with one loop
    # def maximumSwapEff(self, nums):
    #     oarr=list(str(nums))
    #     narr=oarr[:]
    #     for i in range(len(oarr)-1):
    #         oarr[i],oarr[i+1]=oarr[i+1],oarr[i]
    #         if narr<oarr:   narr=oarr[:]
    #         oarr[i],oarr[i+1]=oarr[i+1],oarr[i]
    #     return "".join(narr)

# nums=28396
nums = 98368
s=Solution()
print(s.maximumSwap(nums))
# print(s.maximumSwapEff(nums))
