# https://leetcode.com/problems/longest-increasing-subsequence
    # https://leetcode.com/problems/longest-increasing-subsequence/solution/
# https://www.youtube.com/watch?v=cjWnW0hdF1Y&ab_channel=NeetCode
# longest increasing subsequence
    
'''
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

For each element i, check all the elements before it using second for loop
if element at i is greater than element at j
then dp[i]=max(dp[i], dp[j]+1)
'''

class Solution:
    def lengthOfLIS(self, nums):
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

nums = [10,2,5,3,101]
obj=Solution()
print(obj.lengthOfLIS(nums))
