'''
https://leetcode.com/problems/add-strings
add two number
add strings

same as:
# add two linked list
# add linked list
# https://leetcode.com/problems/add-two-numbers-ii/submissions/
'''
        
    def addStrings(self, num1, num2):
        res=[]
        carry=0
        p1=len(num1)-1
        p2=len(num2)-1
        
        while p1>=0 or p2>=0:
            x1=ord(num1[p1]) - ord('0') if p1>=0 else 0
            x2=ord(num2[p1]) - ord('0') if p2>=0 else 0
            val=(carry+x1+x2) % 10
            carry=(carry+x1+x2)//10
            p1-=1
            p2-=1
            res.append(val)
        if carry:   res.append(carry)
        
        return ''.join(str(x) for x in res[::-1])
            
        

s=Solution()
print(s.addStringsEasy("24", "10"))


'''
class Solution(object):
    def addStringsEasy(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def convert(c):
            return ord(c)-ord('0')
        
        x1=x2=0
        for i in num1:
            x1=x1*10+convert(i)
        for j in num2:
            x2=x2*10+convert(j)
        
        return x1+x2
'''