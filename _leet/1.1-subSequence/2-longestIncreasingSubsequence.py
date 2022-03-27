# https://leetcode.com/problems/longest-increasing-subsequence
    # https://leetcode.com/problems/longest-increasing-subsequence/solution/
# https://www.youtube.com/watch?v=cjWnW0hdF1Y&ab_channel=NeetCode
# longest increasing subsequence
    

'''
dynamic programming

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

For each element i, check all the elements before it using second for loop
if element at i is greater than element at j
then dp[i]=max(dp[i], dp[j]+1)

Algorithm
Initialize an array dp with length nums.length and all elements equal to 1. 
    dp[i] represents the length of the longest increasing subsequence that ends with the element at index i.

Iterate from i = 1 to i = nums.length - 1.
    At each iteration, use a second for loop to iterate from j = 0 to j = i - 1 (all the elements before i). 
    For each element before i, check if that element is smaller than nums[i]. 
        If so, set dp[i] = max(dp[i], dp[j] + 1).

Return the max value from dp.
'''

class Solution:
    def lengthOfLIS(self, nums):
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

nums = [10,2,5,3,101]   #2,3,101
obj=Solution()
print(obj.lengthOfLIS(nums))

