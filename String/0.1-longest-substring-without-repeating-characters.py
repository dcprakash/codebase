'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/
sliding window
same concept as minimum-window-substring

We use HashSet to store the characters in current window [i, j)[i,j) (j = ij=i initially). 
Then we slide the index jj to the right. If it is not in the HashSet, we slide jj further. 
Doing so until s[j] is already in the HashSet. 
At this point, we found the maximum size of substrings without duplicate characters start with index i. 
If we do this for all ii, we get our answer.
'''

class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		chars = [0]*128
		
		left = right = 0
		
		res=0
		while right<len(s):
			r=s[right]
			chars[ord(r)]+=1
			print(ord(r))
			print(chars)
			
			while chars[ord(r)] > 1:
				l=s[left]
				chars[ord(l)]-=1
				left+=1
			
			res=max(res, right-left+1)
			right+=1
		
		return res

s=Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
