class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def baktract(ix=0):
            if ix==n:   result.append([nums[:]])
            for i in range(ix, n):
                nums[i], nums[ix] = nums[ix], nums[i]
                baktract(ix+1)
                nums[i], nums[ix] = nums[ix], nums[i]
            
            
            
        
        

        
s=Solution()
print(s.combinationSum([2,3,6,7]))