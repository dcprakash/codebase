'''
https://leetcode.com/problems/3sum-smaller/

3 sum smaller
taget sum smaller
'''


class Solution:
    def threeSumSmaller(self, nums, target):
        nums.sort()
        n=len(nums)
        res=0
        for i in range(n-2):
            l=i+1
            r=n-1
            while l<r:
                if nums[i]+nums[l]+nums[r]<target:  #IF THREESUM < TARGET, THEN BECAUSE THEE ARRAY IS SORTED
                    res+=r-l    #ALL NUMBERS IN BETWEEN WILL ALSO BE LESS OR EQUAL TO K AND THEREFORE BE VALID ANSWERS
                    l+=1
                else:
                    r-=1
        return res
        

sol=Solution()
print(sol.threeSumSmaller([-2,0,1,3],2))