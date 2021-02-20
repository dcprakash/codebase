# Python3 program for right rotation of an array (Reversal Algorithm) 


# Function to reverse arr 
# from index start to end 
def reverseArray( arr, start, end): 
	
	while (start < end): 
		
		arr[start], arr[end] = arr[end], arr[start] 
		start = start + 1
		end = end - 1
	

# Function to right rotate arr 
# of size n by d 
def rightRotate(arr, r, n): 
	reverseArray(arr, 0, n - 1); 
	reverseArray(arr, 0, r- 1); 
	reverseArray(arr, r, n - 1); 


# function to pr an array 
def prArray( arr, size): 
	for i in range(0, size): 
		print (arr[i]) 


# Driver code 
arr = [1, 3, 4, 6] 
n = len(arr) 
r = 1
	
# Function call 
rightRotate(arr, r, n) 
prArray(arr, n) 

b = [1, 3, 4, 6]
print(b[n-r:]+b[0:n-r])