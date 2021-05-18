"""
https://leetcode.com/problems/house-robber

max sum without adjacent
max sum without alternate

dynamic program
"""
class Solution:
    def rob(self, nums):
        incl=0
        excl=0
        for i in nums:
            new_excl=max(incl, excl)
            incl=excl+i
            excl=new_excl
        return max(incl, excl)
        
obj=Solution()
print(obj.rob([2,7,9,3,1]))