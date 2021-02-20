'''
Given a binary string, count number of substrings that start and end with 1. 
For example, if the input string is “00100101”, 
    then there are three substrings “1001”, “100101” and “101”.
'''

s="01101"
n=len(s)
count=0
for i in range(n):
    if s[i]=="1":
        for j in range(i+1,n):
            if s[j]=="1":
                count+=1
            else:
                continue
print(count)