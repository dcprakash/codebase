# https://leetcode.com/problems/reverse-words-in-a-string-iii/

# s = "Let's take LeetCode contest"
# res=[]
# for word in s.split(' '):
#     res.append(word[::-1])
# print(" ".join(res))

# reverse words
# reverse string

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(word[::-1] for word in s.split(' '))

obj=Solution()
print(obj.reverseWords("Let's take LeetCode contest"))