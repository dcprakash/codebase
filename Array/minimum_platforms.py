# Program to find minimum 
# number of platforms  
# required on a railway 
# station 

# // https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/
# // Input:  arr[]  = {9:00,  9:40, 9:50,  11:00, 15:00, 18:00}
# //         dep[]  = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}
# // Output: 3
# // There are at-most three trains at a time (time between 11:00 to 11:20)

# // Program to find minimum number of platforms 
# // required on a railway station 

  
# Returns minimum number 
# of platforms reqquired 
def findPlatform(arr,dep,n): 
  
    # Sort arrival and 
    # departure arrays 
    # works even without these
    arr.sort() 
    dep.sort() 
    print(arr)
    print(dep)
   
    # plat_needed indicates 
    # number of platforms 
    # needed at a time 
    plat_needed = 1
    result = 1
    i = 1
    j = 0
   
    # Similar to merge in 
    # merge sort to process  
    # all events in sorted order 
    while (i < n and j < n): 
     
        # If next event in sorted 
        # order is arrival,  
        # increment count of 
        # platforms needed 
        if (arr[i] < dep[j]): 
          
            plat_needed+=1
            i+=1
   
            # Update result if needed  
            if (plat_needed > result):  
                result = plat_needed 
          
   
        # Else decrement count 
        # of platforms needed 
        else: 
          
            plat_needed-=1
            j+=1
          
    return result 
  
# driver code 
  
arr = [900, 940, 950, 1100, 1500, 1800] 
dep = [910, 1200, 1120, 1130, 1900, 2000] 
n = len(arr) 
  
print("Minimum Number of Platforms Required = ", 
        findPlatform(arr, dep, n)) 