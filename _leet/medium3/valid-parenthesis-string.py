"""
https://leetcode.com/problems/valid-parenthesis-string/

valid-parenthesis-string
balance parenthesis

'(()())' is valid, we had a balance of 1, 2, 1, 2, 1, 0

(***)	has below possibilities

(		(

(*		()0		(*1		((2

(**		(*)0,	(()1,	((*2,	(((3

(***	(**)0	((*)1	((**	(((3	((((4

(***)	(***)0	((*)1	((()2	(((()3


above possibilities get us [lo, hi] = [1, 1], [0, 2], [0, 3], [0, 4], [0, 3]

Let lo, hi respectively be the smallest and largest possible number of open left brackets
	after processing the current character in the string.

If we encounter a left bracket (c == '('), then lo++, otherwise we could write a right bracket, so lo--
if we encounter a right bracket c==')' then hi--
if c is not ')', then high++ bcz this char can be ( or *
if high is < 0 then break
if low <0, make low 0 as we can never be less than 0

return balanced, at the end if if low=0


When checking whether the string is valid, we only cared about the "balance": 
    the number of extra, open left brackets as we parsed through the string. 
    For example, when checking whether '(()())' is valid, 
    we had a balance of 1, 2, 1, 2, 1, 0 as we parse through the string
    
    


"""
class Solution(object):
    def checkValidString(self, s):
        lo = hi = 0
        for c in s:
            lo += 1 if c == '(' else -1 # when ) we do lo--
            hi += 1 if c != ')' else -1 #i.e., if c in ('(','*'); when ) we do hi--
            if hi < 0: break
            lo = max(lo, 0)

        return lo == 0
        
s = "(*)"
val=Solution()
print(val.checkValidString(s))