"""
https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
"""

def reverse(s):
    strs=""
    for i in s:
        strs = i + strs
        # print strs
    return strs

if __name__ == '__main__':
    s = "Geeksforgeeks"
      
    print ("The original string is : ") 
    print (s) 
      
    print ("The reversed string is : ") 
    print (reverse(s)) 


# print("\n \n")
# print "************method2************"
# len = len(s)-1
# str2 = ""
# while len >= 0:
#     str2+=s[len]
#     len -=1
# print(str2)


# print("\n \n")
# print "************method3************"
# print(s[::-1])



# print("\n \n")
# print "************method4************"
# s="Geeksforgeeks"
# s2=""
# for i in range(len(s)-1,-1,-1):
# 	s2+=s[i]
# print(s2)