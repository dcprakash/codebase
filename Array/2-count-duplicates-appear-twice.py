# https://leetcode.com/problems/find-the-duplicate-number/


from collections import Counter

# returns all duplicates
def findDuplicate(nums):
    count=Counter(nums)
    res=[k for k,v in count.items() if v>1]
    return res if res else []


# returns first duplicate occurence
def findDuplicateEff(nums):
    nums.sort()
    # this can also return 2 but it has appearer more than twice
    # [1,2,2,2,3,4,4,5]
    # 4 is correct answer
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return nums[i]
            

nums=[2,2,3,2,3]
print(findDuplicate(nums))