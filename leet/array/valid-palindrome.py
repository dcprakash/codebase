# https://leetcode.com/problems/valid-palindrome/solution/

s="A man, a plan, a canal: Panama"

# check if item evaluates to true in the func, if so keep it
# The isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers)
alnum=filter(lambda ch: ch.isalnum(), s)

# map applies lambda lower function to each item in s
slower=map(lambda ch: ch.lower(), alnum)

str1="".join(slower)
str2=str1[::-1]

if str1==str2:
    print("Palindrome")
else:
    print("Not Palindrome")