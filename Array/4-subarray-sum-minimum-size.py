# https://leetcode.com/problems/minimum-size-subarray-sum/


def minSubArrayLen(s, nums):
    res=float('inf')
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sum=0
            for k in range(i,j+1):
                sum+=nums[k]
            if sum>=s:
                res=min(res,j-i+1)
                break
    return res if res!=float('inf') else 0
    

'''
1. sum all nums in array until sum>=s
2. start subtracting left most value of array and sum until sum<s 
    2.1 keep track of minimum count
'''
def minSubArrayLenEfficient(s, nums):
    res=float('inf')
    left=sum=0
    for i in range(len(nums)):
        sum+=nums[i]
        while sum>=s:
            res=min(res, i+1-left)
            sum-=nums[left]
            left+=1
    return res if res!=float('inf') else 0
        

s = 5
nums = [2,3,1,2,4,3]
# print(minSubArrayLen(s, nums))
print(minSubArrayLenEfficient(s, nums))