# https://leetcode.com/problems/find-the-duplicate-number/


from collections import Counter

def findDuplicate(nums):
    count=Counter(nums)
    res=[k for k,v in count.items() if v==2]
    return res[0] if res else []


def findDuplicateEff(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return nums[i]
            

nums=[2,2,2,2,2]
print(findDuplicate(nums))