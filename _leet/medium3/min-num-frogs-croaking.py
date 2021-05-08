'''
https://leetcode.com/problems/minimum-number-of-frogs-croaking/

substring occurence in string
froag croak

'''

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        
        # a list of counters to record the appearances [ #'c', #'r', #'o', #'a', #'k' ]
        counters = [0] * 5
        
        # frogs detected
        frogs = 0
        
        
        for char in croakOfFrogs:
            
            # if unexpected char ( not in 'croak' ) appears, return -1
            if char not in 'croak':
                return -1
            
            # update the counters, where does this char appeah in croak
            ind = 'croak'.index(char)
            counters[ind] += 1
            
            # if misplacement happends (later char appears earlier than prev one), return -1
            if ind > 0 and counters[ind-1] < counters[ind]:
                return -1
            
            # update the maximum detected frogs
            frogs = max(frogs, max(counters) - min(counters))
            
            
        # return -1 if the string is incomplete
        return frogs if len(set(counters)) == 1 else -1 


s=Solution()
# print(s.minNumberOfFrogs("croakcroak"))
print(s.minNumberOfFrogs("crcoakroak"))
