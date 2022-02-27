# https://www.geeksforgeeks.org/equilibrium-index-of-an-array/
"""

Input: A[] = {-7, 1, 5, 2, -4, 3, 0}
Output: 3
3 is an equilibrium index, because:
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]

"""
# Python program to find the equilibrium 
# index of an array 
  
# function to find the equilibrium index 
def equilibrium(arr): 
  
    # finding the sum of whole array 
    total_sum = sum(arr) 
    leftsum = 0
    for i, num in enumerate(arr): 
          
        # total_sum is now right sum 
        # for index i 
        total_sum -= num
        #print("RighSum {}".format(total_sum))
        
        #print("LeftSum {} \n".format(leftsum))
        if leftsum == total_sum: 
            return i 
        leftsum += num 
        
       
      # If no equilibrium index found,  
      # then return -1 
    return -1
    
def equilibriumEasy(arr):
    n = len(arr) 
  
    for i in range(n): 
        leftsum = 0
        rightsum = 0
      
        # get left sum 
        for j in range(i): 
            leftsum += arr[j] 
          
        # get right sum 
        for j in range(i + 1, n): 
            rightsum += arr[j] 
          
        # if leftsum and rightsum are same, then we are done 
        if leftsum == rightsum: 
            return i 
      
    # return -1 if no equilibrium index is found 
    return -1

      
# Driver code 
arr = [1, 3, 5, 2, 2]
print ('First equilibrium index is Efficient  ', equilibrium(arr)) 
print ('First equilibrium index is EasyMethod ', equilibriumEasy(arr)) 
