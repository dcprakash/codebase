# program to check if a string is two time rotation of another string. 
# https://www.geeksforgeeks.org/check-string-can-obtained-rotating-another-string-2-places/
# string rotation
# array rotation
# Check if a string can be obtained by rotating another string 2 places

def isRotated(str1, str2): 
    print("str1 = {}".format(str1))
    print("str2 = {}".format(str2))
    
    if (len(str1) != len(str2)): 
        return False
  
    clock_rot = "" 
    anticlock_rot = "" 
    l = len(str2) 
  
    # Initialize string as anti-clockwise rotation 
    print(str2[l - 2:]+ "    " + str2[0: l - 2])
    anticlock_rot = (anticlock_rot + str2[l - 2:] + 
                                     str2[0: l - 2]) 
      
    # Initialize string as clock wise rotation 
    print(str2[2:] + "    " + str2[0:2])
    clock_rot = clock_rot + str2[2:] + str2[0:2] 
  
    # check if any of them is equal to string1
    if str1 == clock_rot:
        print("rotated clockwise")
    elif str1 == anticlock_rot:
        print("rotated anti-clockwise")
    else:
        print("string does not match")
  
 
# Driver code 
if __name__ == "__main__": 
      
    str1 = "amazon"
    # str2 = "azonam"
    str2 = "onamaz"
isRotated(str1, str2)