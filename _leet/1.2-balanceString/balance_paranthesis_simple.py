

def bracketBalanced(expr):
    balance=0
    for i in expr:
        if i=='(':  balance+=1
        elif i==')':    balance-=1
        if balance<0:
            return False
    return balance==0
                

expr="(a)"
print(bracketBalanced(expr))

'''
-'ve means more )
+'ve means more (
0 means balanced
'''