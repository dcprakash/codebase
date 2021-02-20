# https://practice.geeksforgeeks.org/problems/-rearrange-array-alternately/0/


a=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
# a=['a','a','b']
n=len(a)
l=0
r=n-1
res=[]
rfirst=True
while l<=r:
	if rfirst:
		res.append(a[r])
		r-=1
		rfirst=False
	else:
		res.append(a[l])
		l+=1
		rfirst=True
print(res)



# Given a sorted array of positive integers.

# 1
# 6
# 1 2 3 4 5 6
# 6 1 5 2 4 3 

# Example: 
# Input:
# 2
# 6
# 1 2 3 4 5 6
# 11 
# 10 20 30 40 50 60 70 80 90 100 110

# Output:
# 6 1 5 2 4 3
# 110 10 100 20 90 30 80 40 70 50 60

# Explanation:
# Testcase 1: Max element = 6, min = 1, second max = 5, second min = 2, and so on... Modified array is : 6 1 5 2 4 3.