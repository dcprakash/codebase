'''
https://leetcode.com/problems/contains-duplicate/
    
    
'''


class Solution:
    def containsDuplicate(self, nums):
        d = {}
        for i in nums:
            if i in d:
                return True
            d[i] = 1
        return False


obj = Solution()
print(obj.containsDuplicate([1, 2, 3, 1]))
