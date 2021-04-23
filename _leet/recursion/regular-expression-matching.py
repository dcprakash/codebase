"""
https://leetcode.com/problems/regular-expression-matching/solution/
'.' Matches any single character
'*' Matches zero or more of the preceding element.

if no *, we simply check from left to right if each character of the text matches the pattern
    refer to def match() below; each recursion will parse from index 1 (as long as if parsing for index 0 is true)
    bool(text) retrun True if its not an empty string
    not text returns False

If a star is present in the pattern, it will be in the second position \text{pattern[1]}pattern[1]. 
    Then, we may ignore this part of the pattern
    proceed with recursion if there are more "REMAINING" pattern after * i.e., len(pattern)>2
"""


def match(text, pattern):
    if not pattern: return not text
    first_match = bool(text) and pattern[0] in (text[0])
    # for abc and abc; first we check a,a; then b,b and c,c
    # each time we ensure aa i.e., first_match is met, then
    # call match(bc,bc) if b,b is good, then call match(c,c)
    # if all aa, bb and cc match and no pattern left, retun true
    return first_match and match(text[1:], pattern[1:])
                

def isMatch(text, pattern):
    if not pattern:
        return not text

    first_match = bool(text) and pattern[0] in {text[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':
        return (isMatch(text, pattern[2:]) or
                first_match and isMatch(text[1:], pattern))
    else:
        return first_match and isMatch(text[1:], pattern[1:])


# text = "aa"
# pattern = "a*"

text = "aab"
pattern = "c*a*b"

# print(match(text,pattern))
print(isMatch(text,pattern))
