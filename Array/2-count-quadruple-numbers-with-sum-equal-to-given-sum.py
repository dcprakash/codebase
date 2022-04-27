'''
https://leetcode.com/problems/4sum/
4 sum
'''

class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        n=len(nums)
        res=[]
        for i in range(n-3):
            for j in range(i+1,n-2):
                l=j+1
                r=n-1
                while l<r:
                    if nums[i]+nums[j]+nums[l]+nums[r]==target:
                        if [nums[i],nums[j],nums[l],nums[r]] not in res:
                            res.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                    elif nums[i]+nums[j]+nums[l]+nums[r]>target:
                        r-=1
                    else:
                        l+=1
        return res
        

sol=Solution()
print(sol.fourSum([-3,-1,0,2,4,5],2))