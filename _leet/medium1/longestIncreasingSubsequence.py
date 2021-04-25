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
    lis=[1]*len(nums)
    for i in range(len(nums)-1, -1, -1):
        for j in range(i+1, len(nums)):
            if nums[i]<nums[j]:
                lis[i]=max(lis[i], 1+lis[j])
    return max(lis)

    
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
nums = [10,2,5,3,101]
# nums = [2,1,3,4]
# print(longestIncreasingSubsequence(nums))
print(LongestIncreasingSequence(nums))
# print(longestIncreasingSubsequenceCorrect(nums))


'''
      0.  1. 2. 3. 4. 
list=[1,  1, 1, 1, 1]
nums=[10, 2, 5, 3, 101]
     [1,  1, 1, 1, 1]
     [1,  1, 1, 2, 1]
     [1,  1, 2, 2, 1]
     [1,  3, 2, 2, 1]
 max([2,  3, 2, 2, 1])  =   3

For each value we have 2 choice, include or not
keep iterating for taken, until we find decreasing value
don't include decreasing value:
    if we dont include, get values for "not taken"
return max(taken, nottaken)


'''
    