'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
1. Use brute force method to check if each substring is unique
2. for each substring check if all are unique
3. keep score of max unique substring in ans
length longest substring


We use HashSet to store the characters in current window [i, j)[i,j) (j = ij=i initially). 
Then we slide the index j to the right. If it is not in the HashSet, we slide j further. 
Doing so until s[j] is already in the HashSet. 
At this point, we found the maximum size of substrings without duplicate characters start with index i. 
Since j found first duplicate, add this char to hash set and remove ith character from hashset (it would be same char);
    also move left index +1, to slide window forward
If we do this for all i, we get our answer.

# sliding window
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check(start, end):
            chars = [0] * 128
            for i in range(start, end + 1):
                c = s[i]
                chars[ord(c)] += 1
                if chars[ord(c)] > 1:
                    return False
            return True

        n = len(s)

        res = 0
        for i in range(n):
            for j in range(i, n):
                if check(i, j):
                    res = max(res, j - i + 1)
        return res
        
        
    def lengthOfLongestSubstringEff(self, s: str) -> int:
        chars = [0] * 128

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1

            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1

            res = max(res, right - left + 1)

            right += 1
        return res

s=Solution()
# print(s.lengthOfLongestSubstring("abca"))
print(s.lengthOfLongestSubstringEff("abca"))

