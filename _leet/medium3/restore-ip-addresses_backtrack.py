'''
https://leetcode.com/problems/restore-ip-addresses/

ip address validate
restore ip address
backtrack
'''


class Solution:
    def restoreIpAddresses(self, s):    
        def backtrack(comb, start):
            nonlocal res
            if len(comb) == 4:   
                if start == len(s):     # when start ix reached end, we dont have any digits left
                    res.append(".".join(comb))
                return
            for i in range(start, min(start+3, len(s))):    #0 to min(0+3, len(s))
                """
                Check if the comb segment is valid :
                1. the first character could be '0' 
                   only if the segment is equal to '0'; if not continue
                2. greater than or equal 0 "AND" less or equal to 255      
                
                """
                if s[start] == '0' and i > start:
                    continue
                if 0 <= int(s[start:i+1]) <= 255:
                    backtrack(comb + [s[start:i+1]], i + 1)
        
        res = []
        backtrack([], 0)
        
        return res

s=Solution()
# print(s.restoreIpAddresses("25525511135"))
print(s.restoreIpAddresses("101023"))