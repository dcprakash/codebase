# check if string is balanced


def bracketBalanced(expr):
    stack = []
    for c in expr:
        if c in ("(", "{", "["):
            stack.append(c)
        elif c.isalnum():
            stack.append(c)
        else:
            if not stack:
                return False
            
            cur=stack.pop()
            if cur.isalpha():
                stack.pop()
                
            if cur == "(":
                if c != ")":
                    return False
            if cur == "{":
                if c != "}":
                    return False
            if cur == "[":
                if c != "]":
                    return False
    if stack:
        return False
    else:
        return True
                

expr="(a))"
print(bracketBalanced(expr))
