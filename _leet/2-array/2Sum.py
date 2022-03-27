# key pair sum


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




# def findDupletSum(A, n, X): 

# 	A.sort() 
# 	l=0
# 	r=n-1
			
# 	while (l < r): 
# 		if(A[l] + A[r] == X): 
# 			print(A[l], ",", A[r]) 
# 			l += 1
# 			r -= 1
		
# 		elif (A[l] + A[r] < X): 
# 			l += 1
# 		elif (A[l] + A[r]) > X:
# 			r -= 1


# if __name__ == "__main__": 
	
# 	A = [1, 4, 45, 6, 10, 12]	# 1 4 6 10 12 45
# 	X = 16
# 	n = len(A) 
# 	findDupletSum(A, n, X) 

