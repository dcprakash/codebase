# https://leetcode.com/problems/longest-increasing-subsequence/solution/
# https://www.youtube.com/watch?v=cjWnW0hdF1Y&ab_channel=NeetCode


def longestIncreasingSubsequence(nums):
    n=len(nums)
    msf=0
    for i in range(n):
        for j in range(i,n):
            if nums[i]>nums[j]:   break
            else:   msf=max(msf,j-i)
    return msf
    
def longestIncreasingSubsequenceCorrect(nums):
    def lengthOfLIS(nums, prv, cur):
        n=len(nums)
        if cur==n:  return 0
        
        taken=0
        if nums[cur] > prv:
            taken = 1 + lengthOfLIS(nums, nums[cur], cur+1)
            
        notTaken = lengthOfLIS(nums, prv, cur+1)
        return max(taken, notTaken)
    
    return lengthOfLIS(nums, -float('inf'), 0)
    

# nums = [10,9,2,3,7,101,18]
# nums = [10,9,2,5,3,7,101,18]
nums = [2,1,3,4]
# print(longestIncreasingSubsequence(nums))
print(longestIncreasingSubsequenceCorrect(nums))
    