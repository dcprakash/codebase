'''
https://leetcode.com/problems/robot-bounded-in-circle/

# robot circle path
'''

N=0
E=1
S=2
W=3

def isRobotBounded(instructions):
    x=y=0
    d=N
    for i in instructions:
        if i=="R":  d=(d+1)%4
        elif i=="L":    d=(d-1+4)%4
        else:
            if d==N:    y+=1
            elif d==E:    x+=1
            elif d==S:    y-=1
            else:    x-=1  # d==W
    
    return (x==0 and y==0) or d!=N


instructions="GL"
# instructions="GGLLGG" # robot does NOT face north, return False
print(isRobotBounded(instructions))
