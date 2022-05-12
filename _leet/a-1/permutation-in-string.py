'''
https://leetcode.com/problems/permutation-in-string/
https://www.youtube.com/watch?v=UbyhOgBN834&ab_channel=NeetCode

similar to 1-minimum-window-substring.py, remove-minimum-number-characters-two-strings-become-anagram-2.py

look for anagram, dont care about order
sliding window, then sort and compare if both string are anagram
lower alphabets so 26 chars so create hashmap of 26 for each string

matches=0 (to avoid comparing 26 chars in each iteration)
    does a count of s1 and s2 match if so matches+=1
    once we have 26 matches in s1 and sliding window of s2; we are good to go
    


'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        # s1=[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ...]
        # s2=[0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, ...]
        
        # first and only one time, compare 2 strings and update matches
        # for given input, we get 24 matches
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        l = 0
        # we start from len(s1) bcz we already initialized both s1 and s2 above upto len(s1)
        for r in range(len(s1), len(s2)):
            if matches == 26: return True
            
            # update s2 hashmap at char index
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:    #after adding char from sliding window, if count of char in s1 and s2 match
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:  #count of char in s1 and s2 were equal before we move the window, but now not equal
                matches -= 1

            # move left sliding window, means decrement char count of s2 at index             
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
    
s=Solution()
print(s.checkInclusion("ab", "eabc"))