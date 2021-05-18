'''
https://leetcode.com/problems/fibonacci-number/

fib(n)=fib(n-1)+fib(n-2)

fibonacci of 4
0 then 1
1 then 1

        fib(3)      +       fib(2)
    fib(1)+fib(2)       fib(1)+fib(0)
    
dynamic programing
'''

class Solution:
    def fib(self, n):
        if n<=1:    return n
        return self.fib(n-1) + self.fib(n-2)
        
    def fibMemo(self, n):
        def helper(n):
            cache={0:0, 1:1}
            for i in range(2,n+1):
                cache[i]=cache[i-1]+cache[i-2]
            return cache[n]
        
        if n<=1:    return n
        return helper(n)
        
        
        
obj=Solution()
print(obj.fib(4))
print(obj.fibMemo(4))
