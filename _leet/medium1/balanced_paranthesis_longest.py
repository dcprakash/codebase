# return count of balanced string


def bracketBalanced(s):
    stack = []
    max_p=0
    for c in range(len(s)):
        if s[c] in ("("):
            stack.append(s[c])
        else:
            if stack and s[c]==')':
                stack.pop()
                max_p+=1
    return max_p*2
                

expr="()(()"
print(bracketBalanced(expr))
