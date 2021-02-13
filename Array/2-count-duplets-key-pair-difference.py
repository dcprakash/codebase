# https://leetcode.com/problems/k-diff-pairs-in-an-array/solution/
# count duplet key pair differences, K diff pairs in array

def findPairs(nums, k, n):
    l=0
    r=1
    count=0
    while l<n and r<n:
        if l==r or nums[r]-nums[l]<k:
            r+=1
        elif nums[r]-nums[l]>k:
            l+=1
        else:
            l+=1
            count+=1
            while l<n and nums[l]==nums[l-1]:
                l+=1
    return count
        

nums = [3,1,4,1,5]  # 1,1,3,4,5
k = 3
print(findPairs(sorted(nums), k, len(nums)-1))