'''
https://leetcode.com/problems/minimum-moves-to-equal-array-elements

'''


class Solution:
    def minMoves(self, nums):
        nums.sort()
        count=0
        for i in range(len(nums)-1,-1,-1):
            count+=nums[i]-nums[0]
        return count

        
s=Solution()
print(s.minMoves([1,2,3]))