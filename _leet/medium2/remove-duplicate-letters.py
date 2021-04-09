'''
https://leetcode.com/problems/remove-duplicate-letters/
https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

arrange smallest
remove duplicates
smallest subsequence (subsequent) distinct characters

As a result any string beginning with a will always be less than any string 
    beginning with b, regardless of the ends of both strings.

Remove as many characters as possible off the top of the stack, and then 
    add the current character

The conditions for deletion are:
    The character is greater than the current characters
    The character can be removed because it occurs later on

'''


class Solution:
    def removeDuplicateLetters(self, s):
        stack = []

        # this lets us keep track of what's in our solution in O(1) time
        seen = set()

        # this will let us know if there are no more instances of s[i] left in s
        last_occurrence = {c: i for i, c in enumerate(s)}   # {'a': 2, 'c': 7, 'b': 6, 'd': 4}


        for i, c in enumerate(s):

            # we can only try to add c if it's not already in our solution
            # this is to maintain only one of each character
            if c not in seen:
                # if the last letter in our solution:
                #    1. exists
                #    2. is greater than c so removing it will make the string smaller
                #    3. it's not the last occurrence
                # we remove it from the solution to keep the solution optimal
                while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
        return ''.join(stack)
        
        
# string = "cbacdcbc"
string = "bcabc"

s=Solution()
print(s.removeDuplicateLetters(string))
