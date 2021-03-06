# https://leetcode.com/problems/longest-increasing-subsequence/solution/
# https://www.youtube.com/watch?v=cjWnW0hdF1Y&ab_channel=NeetCode


# def longestIncreasingSubsequence(nums):
#     n=len(nums)
#     msf=0
#     for i in range(n):
#         res=nums[i]
#         for j in range(i+1,n):
#             res=max(res,nums[j])
#             if res>nums[j]:   
#                 continue
#             else:
#                 msf=max(msf,j-i+1)
#     return msf
    
    
def LongestIncreasingSequence(nums):
    res=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]>nums[j]: 
                break
            else:
                res=max(res, j-i)
    return res            

    
def longestIncreasingSubsequenceCorrect(nums):
    
    def lengthOfLIS(nums, prv, cur):
        if cur==len(nums):  
            return 0
        
        taken=0
        if nums[cur] > prv:
            taken = 1 + lengthOfLIS(nums, nums[cur], cur+1)
            
        notTaken = lengthOfLIS(nums, prv, cur+1)
        return max(taken, notTaken)
    
    return lengthOfLIS(nums, -float('inf'), 0)
    

# nums = [10,9,2,3,7,101,18]
# nums = [10,9,2,5,3,7,101,18]
nums = [3,5]
# nums = [2,1,3,4]
# print(longestIncreasingSubsequence(nums))
# print(LongestIncreasingSequence(nums))
print(longestIncreasingSubsequenceCorrect(nums))


'''
For each value we have 2 choice, include or not
keep iterating for taken, until we find decreasing value
don't include decreasing value:
    if we dont include, get values for "not taken"
return max(taken, nottaken)


'''
    