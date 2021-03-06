'''
https://leetcode.com/problems/permutations/submissions/

permutation of 3 chars is 3*2*1=6

			123
	23		 13		12
  3    2    3  1   2  1

for every value in num
	remove first value of 3
	then take permutation of remaining 2 values
	after getting permutation, append the popped value and add to result
	before backtracking, add popped value back to original (this time it'll be appended to end of array)

a=[1,2,3]
copy list b=a[:]
When you omit the start index and the end index from the slice, then your slice will start from the beginning of the list all the way to the end of the list.
https://www.afternerd.com/blog/python-copy-list/

'''

class Solution:
	def permute(self, nums):

		def backtrack(ix=0):
			if ix==n:	output.append(nums[:])
			for i in range(ix, n):
				nums[ix],nums[i]=nums[i],nums[ix]
				backtrack(ix+1)
				nums[ix],nums[i]=nums[i],nums[ix]

		n=len(nums)
		output=[]
		backtrack()
		
		return output
	

nums=[1,2,3]
# nums=[1]
s=Solution()
print(s.permute(nums))
		