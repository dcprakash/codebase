# Python implementation of the above approach 

# Function to print product array for a given array 
# arr[] of size n 

# https://www.geeksforgeeks.org/a-product-array-puzzle/
# prod[i] is equal to the product of all the elements of arr[] except arr[i]
# Product array
# a[]=	10 3 5
# l[]=	1 10 30
# r[]=	15 5 1
# p[]=	15,50,30
'''
https://leetcode.com/problems/product-of-array-except-self/
product of array
'''


def productArray(arr, n): 

	# Base case 
	if(n == 1): 
		print(0) 
		return
		
	# Allocate memory for temporary arrays left[] and right[] 
	left = [0]*n 
	right = [0]*n 

	# Allocate memory for the product array 
	prod = [0]*n 

	# Left most element of left array is always 1 
	left[0] = 1

	# Rightmost most element of right array is always 1 
	right[n - 1] = 1

	# Construct the left array 
	for i in range(1, n): 
		left[i] = arr[i - 1] * left[i - 1] 

	# Construct the right array 
	for j in range(n-2, -1, -1): 
		right[j] = arr[j + 1] * right[j + 1] 

	# Construct the product array using 
	# left[] and right[] 
	for i in range(n): 
		prod[i] = left[i] * right[i] 

	# print the constructed prod array 
	for i in range(n): 
		print(prod[i]) 


# Driver code 
arr = [10, 3, 5, 6, 2] 
n = len(arr) 
print("The product array is:") 
productArray(arr, n) 

# This code is contributed by ankush_953 
# a[]=	10 3 5
# l[]=	1 10 30
# r[]=	15 5 1
# p[]=	15,50,30

l=r=[0]*n
l[0]=1
r[n-1]=1
for i in range(1,n-1):
	l[i]=arr[i-1]*l[i-1]