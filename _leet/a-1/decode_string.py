'''
1. maintain two stacks:
    stack = to keep track of occuring chars
    num_stack = to keep track of occuring numers
    note: stack[1] is char that must be repeated num_stack[1] times
2. while iterating, if we encounrter ']', then pop from above 2 stacks
    store multiplication of 2 stacks in stack[-1] i.e., at last element
    
https://leetcode.com/problems/decode-string/submissions/
'''

class Solution:
    def decodeString(self, s):
        
        left = 0
        stack = [""]
        num_stack = []
        while left < len(s):
            if s[left].isdigit():       
                digit = ""
                # Convert the string to int as it can double digits
                while s[left].isdigit():
                    digit += s[left]
                    left += 1
                
                digit_int = int(digit)
                num_stack.append(digit_int)  
                stack.append("")              
            elif s[left] == ']':                    
                mul_string = num_stack.pop()
                top_str = stack.pop()                    
                stack[-1] += mul_string * top_str
            else:
                stack[-1] += s[left]
            left += 1       

        return stack[0]


s = Solution()
string = "3[a2[c]]"
print(s.decodeString(string))
