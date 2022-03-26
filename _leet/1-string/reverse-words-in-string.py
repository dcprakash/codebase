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


# reverse Words
words = "i.like.this.program.very.much".split('.')
n = len(words)
print n
while (n != 0):
    print words[n - 1]
    n = n - 1

print "\n \n"
string = "i.like.this.program.very.much"
list = string.split('.')
i= len(list) - 1
word = ""
while (i>=0):
    word += str(list[i])+'.'
    i -= 1
print word