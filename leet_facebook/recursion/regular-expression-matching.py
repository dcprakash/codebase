"""
https://leetcode.com/problems/regular-expression-matching/solution/

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
        print(not text)
        return not text

    first_match = bool(text) and pattern[0] in {text[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':
        return (isMatch(text, pattern[2:]) or
                first_match and isMatch(text[1:], pattern))
    else:
        return first_match and isMatch(text[1:], pattern[1:])


text = "aa"
pattern = "a*"
print(match(text,pattern))
print(isMatch(text, pattern))
