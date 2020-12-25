# https://www.geeksforgeeks.org/element-equal-to-the-sum-of-all-the-remaining-elements/
# Python 3 implementation of  
# the above approach 
"""
Given an array of N positive elements. 
The task is to find an element which is equal to the sum of all elements of array except itself.
Input: arr[] = {1, 2, 3, 6}
Output: 6
6 is the element which is equal to the sum of all 
remaining elements i.e. 1 + 2+ 3 = 6

sum=12
12-1!=1
12-2!=2
12-3!=3
12-6==6

"""
# Function to find the element 
def findEle(arr, n) : 
      
    # sum is use to store  
    # sum of all elements  
    # of array  
    sum = 0
      
    for i in range(n) : 
        sum += arr[i] 
      
    # iterate over all elements 
    for i in range(n) : 
        if arr[i] == sum - arr[i] : 
            return arr[i] 
      
    return -1
  
# Driver Code 
if __name__ == "__main__" : 
      
    arr = [1, 2, 3, 6 ] 
    n = len(arr) 
    print(findEle(arr, n)) 