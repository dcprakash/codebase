# https://leetcode.com/problems/subarray-sums-divisible-by-k/
# subarray sums divisible by k
# list comp

class Solution:
	def subarraysDivByK(self, A, K) -> int:
		#variable to store our answer
		answer = 0
		n = len(A)

		#loop to maintain the start point of our array
		for start in range(n):
			subarraySum = 0

			#inner loop to go from start till the end
			for end in range(start,n):

				#Adding the current element
				subarraySum += A[end]

				#Checking our condition and updating our answer
				if subarraySum % K == 0:
					answer += 1
		return answer

	'''
	The most optimal solution will be to use hashmaps to store the previous sums(prefixsums).
	But the question "How to check if subarray sum is divisible by k by using prefixSum?" still persists.

	For this, we can store the occurence of prefixSum % k at every iteration.
	If we have already seen this (prefixSum%k), we will add the number of occurences of this to our answer.

	A---------------B
	A------------------------------C
	Let us say if subarray from A to B has sum s and remainder r1 (s%k = r1)
	And if subarray from A to C has sum s1 but remainder r1 (s1%k = r1)

	As the remainder is same, we can definitely say that subarray sum from B to C will definitely be divisible by k.
	'''

	def subarraysDivByKEff(self, nums, k) -> int:
		#Hashmap to store remainders of prefixsum. We have to count the number of subaarays hence storing hashmap[0] = 1 as we have 0 sum at starting
		memo = {0:1}
		answer = 0
		prefixSum = 0

		for i in range(len(nums)):
			prefixSum += nums[i]
			prefixSum %= k
			
			if prefixSum in memo:
				answer += memo[prefixSum]
				memo[prefixSum] += 1
			else:
				memo[prefixSum] = 1
			
		return answer

A = [4,5,0,-2,-3,1]
K = 5

obj=Solution()
print(obj.subarraysDivByK(A,K))
print(obj.subarraysDivByKEff(A,K))