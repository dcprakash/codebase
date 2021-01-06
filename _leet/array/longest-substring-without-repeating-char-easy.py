'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
1. Use brute force method to check if each substring is unique
2. for each substring check if all are unique
3. keep score of max unique substring in ans
'''


def all_unique(str2):
    res=""
    for i in str2:
        if i in res:
            return False
        else:
            res+=i
    return True


def longest_sub_str(str1):
    ans=0
    n=len(str1)
    for i in range(n):
        for j in range(n+1):
            if all_unique(str1[i:j]):
                ans=max(ans,j-i)
    return ans


print(longest_sub_str("abca"))

