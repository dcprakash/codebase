# https://www.geeksforgeeks.org/write-your-own-atoi/
# https://www.youtube.com/watch?v=QyDE7cPycnU&ab_channel=CppNuts
'''
ord('0')=48
ord('1')=49
2       =50
3       =51
res=0*10+(49-48)=1
res=1*10+2=12
res=12*10+3=123
'''

def atoi(s):
    res=0
    sign=1
    i=0
    if s[0]=='-':
        sign=-1
        i+=1
    
    for j in range(i,len(s)):
        res=res*10 + (ord(s[j]) - ord('0'))  # ord returns unicode of given character
    
    return sign * res
    
s="123"
print(atoi(s))




