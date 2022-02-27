# https://leetcode.com/problems/find-the-duplicate-number/
# list comp

from collections import Counter

# returns all duplicates
def findDuplicate(nums) -> int:
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)


'''
All these solution does not use constant space, to acheive problem goal we explore flyod's algorithm
https://leetcode.com/problems/find-the-duplicate-number/solution/

Floyd's algorithm consists of two phases and uses two pointers, usually called tortoise and hare.

In phase 1, hare = nums[nums[hare]] is twice as fast as tortoise = nums[tortoise]. 
Since the hare goes fast, it would be the first to enter the cycle and run around the cycle. 
At some point, the tortoise enters the cycle as well, and since it's moving slower the hare 
    catches up to the tortoise at some intersection point. 
Now phase 1 is over, and the tortoise has lost.

Now the problem is to find the entrance of the cycle.
Note that the intersection point is not the cycle entrance in the general case.

To compute the intersection point, let's note that the hare has traversed twice as many nodes as the tortoise, i.e. 2d(\text{tortoise}) = d(\text{hare})2d(tortoise)=d(hare), implying:

2(F + a) = F + nC + a2(F+a)=F+nC+a, where nn is some integer.

Hence the coordinate of the intersection point is F + a = nCF+a=nC.

In phase 2, we give the tortoise a second chance by slowing down the hare, 
    so that it now moves at the speed of tortoise: tortoise = nums[tortoise], hare = nums[hare]. 
The tortoise is back at the starting position, and the hare starts from the intersection point.
'''

# returns first duplicate occurence
def findDuplicateModifyArray(nums):
    nums.sort()
    # this can also return 2 but it has appearer more than twice
    # [1,2,2,2,3,4,4,5]
    # 4 is correct answer
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return nums[i]
            

nums=[2,2,3,2,3]
print(findDuplicate(nums))