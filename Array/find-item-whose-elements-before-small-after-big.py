# Python3 program to find the element which is greater than 
# all left elements and smaller than all right elements. 
# https://www.geeksforgeeks.org/find-the-element-before-which-all-the-elements-are-smaller-than-it-and-after-which-all-are-greater-than-it/

# find item whose elements before small after big

def findElement(arr, n): 

	# leftMax[i] stores maximum of arr[0..i-1] 
	leftMax = [None] * n 
	leftMax[0] = float('-inf') 

	# Fill leftMax[]1..n-1] 
	for i in range(1, n): 
		leftMax[i] = max(leftMax[i-1], arr[i-1]) 

	# Initialize minimum from right 
	rightMin = float('inf') 

	# Traverse array from right 
	for i in range(n-1, -1, -1): 
	
		# Check if we found a required element 
		if leftMax[i] < arr[i] and rightMin > arr[i]: 
			return i 

		# keep minumum element of arr from right to left 
		rightMin = min(rightMin, arr[i]) 
	
	# If there was no element matching criteria 
	return -1

# Driver program 
if __name__ == "__main__": 
#          0. 1. 2. 3. 4. 5. 6.  7. 8    
	arr = [5, 1, 4, 3, 6, 8, 10, 7, 9] 
	n = len(arr) 
	print("Index of the element is", findElement(arr, n))

'''
[5, 1, 4, 3, 6, 8, 10, 7, 9] 
 5  5  5  5  6  8  10  10 10
						   9
						7
					7
				7
			 6	
'''


'''
Easy approach
for i in range(n):
	for j in range(i,-1,-1):
		a[i]>a[j]
	for k in range(i+1,n)
		a[i]<a[k]
	if j==0 and k==n:
		return i
'''



# small x great
# smallest element after x, should be greater than x
# largest element before x, should be smaller than x
# 0. 1. 2. 3. 4. 5. 6.  7. 8    
# 5, 1, 4, 3, 6, 8, 10, 7, 9	=a

# -0 5  5  5  5  6  8   10 10
                          
#                7  7   7   9 