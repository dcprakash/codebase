# https://practice.geeksforgeeks.org/problems/implement-strstr/1
# string2 present in string1
# string2 substring (sub-string, sub string) of string1
def strstr(s1, s2):
    lenS1 = len(s1)
    lenS2 = len(s2)
    for i in range(0, lenS1 - lenS2 + 1):
        if (s1[i] == s2[0]):
            resultStr = ""
            for j in range(i, i + lenS2):
                resultStr += s1[j]
                if (resultStr == s2):
                    return i

    # i = i+lenP
    return -1

print(strstr("geeks", "ek"))

"""
The function takes two strings as arguments (s,x) 
and  locates the occurrence of the string x in the string s. 
The function returns and integer denoting the first occurrence of the string x in s.
"""