'''

https://leetcode.com/problems/two-sum/

two sum
key pair sum
'''
class Solution:
	def twoSum(self, nums, target):
		seen={}
		for i,v in enumerate(nums):
			remaining=target-v
			if remaining in seen:
				return [seen[remaining], i]
			seen[v]=i
		return []
        
        
obj=Solution()
print(obj.twoSum([2,11,7,15], 9))


'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
'''