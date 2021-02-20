"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/solution/
"""


def removeDuplicates(s):
    n=len(s)
    t=[]
    for i in range(1,n):
        if s[i-1]!=s[i]:
            t.append(s[i-1])
    t.append(s[n-1])
    return "".join(t)
            

'''
one stack for holding unique elements let's say (stack)
another stack (let say counter_stack) for storing current count from the stack.peek( )
Loop through each item in s and adjust/remove top elements of both stacks.
build a return string using both of the stacks.
'''
def removeDuplicatesKchar(s,k):
    stack = []
    counter_stack = []
    for val in s:
        if not stack or stack[-1]!=val:
            stack.append(val)
            counter_stack.append(1)
        elif stack[-1]==val:
            counter_stack[-1]+=1
        if counter_stack[-1]==k:
            counter_stack.pop()
            stack.pop()
    return ''.join([stack[i]*counter_stack[i] for i in range(len(stack))])


s="abbbc"
print(removeDuplicates(list(s)))

# #.   01234
# s = "deeeb"
# k = 3
# print(removeDuplicatesKchar(s,k))



'''
c++
string removeDuplicates(string s, int k) {
    stack<int> counts;
    for (int i = 0; i < s.size(); ++i) {
        if (i == 0 || s[i] != s[i - 1]) {
            counts.push(1);
        } else if (++counts.top() == k) {
            counts.pop();
            s.erase(i - k + 1, k);
            i = i - k;
        }
    }
    return s;
}
'''