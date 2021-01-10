
# return balanced string

'''
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/solution/

add index of ( to stack
ignore alphanumeric, and continue with loop
if ), then pop stack
if ), but stack is empty i.e., nothing to pop
    add this index to be removed
if index elements left in stack; these need to be removed as well
    note: for balanced string stack will be empty
union index to be removed + index inside stack
with for loop, iterate over expression
    if index not in index to be removed:
        add to output string
'''

def bracketBalanced(s):
    stack = []
    ix_to_rm=set()
    
    for i, c in enumerate(s):
        if c not in ("(",")"):
            continue
        if c == "(":
            stack.append(i)
        elif not stack:
            ix_to_rm.add(i)
        else:
            stack.pop()
            
    ix_to_rm=ix_to_rm.union(set(stack))
    
    res=[]
    for i, c in enumerate(s):
        if i not in ix_to_rm:
            res.append(c)
    
    return "".join(res)
            

expr="a)b(c)d"
print(bracketBalanced(expr))
