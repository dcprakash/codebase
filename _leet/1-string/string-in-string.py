'''
https://leetcode.com/problems/ransom-note

string exist in another string

'''
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Check for obvious fail case.
        if len(ransomNote) > len(magazine): return False

        # In Python, we can use the Counter class. It does all the work that the
        # makeCountsMap(...) function in our pseudocode did!
        letters = Counter(magazine)

        # For each character, c, in the ransom note:
        for c in ransomNote:
            # If there are none of c left, return False.
            if letters[c] <= 0:
                return False
            # Remove one of c from the Counter.
            letters[c] -= 1
        # If we got this far, we can successfully build the note.
        return True
        
        
obj=Solution()
ransomNote = "aa"
magazine = "aba"
print(obj.canConstruct(ransomNote, magazine))
