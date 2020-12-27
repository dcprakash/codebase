# https://leetcode.com/explore/interview/card/google/59/array-and-strings/3060/


def compareString(S, T):
    stemp=[]
    ttemp=[]
    i=0
    while i<len(S):
        if S[i]!="#":
            stemp.append(S[i])
            i+=1
        else:
            if stemp:   stemp.pop(-1)
            i+=1
    i=0
    while i<len(T):
        if T[i]!="#":
            ttemp.append(T[i])
            i+=1
        else:
            if ttemp:   ttemp.pop(-1)
            i+=1
    return True if stemp==ttemp else False


def build(string):
    res=[]
    i=0
    while i<len(string):
        if string[i]!="#":
            res.append(string[i])
            i+=1
        else:
            if res:   res.pop(-1)
            i+=1
    return "".join(res)
    

S = "ab##"
T = "c#d#"
# print(compareString(S, T))
print(build(S)==build(T))

    