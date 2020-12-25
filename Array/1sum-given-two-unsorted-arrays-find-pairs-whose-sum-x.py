# https://www.geeksforgeeks.org/given-two-unsorted-arrays-find-pairs-whose-sum-x/

# Python3 program to find all  
# pair in both arrays whose  
# sum is equal to given value x 
  
# Function to find all pairs  
# in both arrays whose sum is 
# equal to given value x 



arr1 = [-1, -2, 4, -6, 5, 7]
arr2 = [6, 3, 4, 0]
x=8

for i in arr1:
    if x-i in arr2:
        print(i,x-i)
        
# def findPairs(arr1, arr2, n, m, x): 
  
#     # Insert all elements of  
#     # first array in a hash 
#     s = set() 
#     for i in range (0, n): 
#         s.add(arr1[i]) 
#     print(s)
#     # Subtract sum from second  
#     # array elements one by one  
#     # and check it's present in 
#     # array first or not 
#     for j in range(0, m): 
#         # can also just do this
#         # if ((x - arr2[j]) in arr1): 
#         if ((x - arr2[j]) in s): 
#             print((x - arr2[j]), '', arr2[j]) 
  
# # Driver code 
# arr1 = [1, 0, -4, 7, 6, 4] 
# arr2 = [0, 2, 4, -3, 2, 1] 
# x = 8
  
# n = len(arr1) 
# m = len(arr2) 
# findPairs(arr1, arr2, n, m, x) 

# """
# 8-0 in arr1 ? no
# 8-2 in arr1 ? yes
# 8-4 in arr1 ? yes
# 8-3 in arr1 ? no
# 8-2 in arr1 ? yes
# 8-1 in arr1 ? yes

# """