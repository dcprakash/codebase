

def moveZero(a):
    c=0
    res=[]
    for i in range(len(a)):
        if a[i]==0:
            c+=1
        else:
            res.append(a[i])
    while c:
        res.append(0)
        c-=1
    print(res)


def moveZeroInPlace(a):
    n=len(a)-1
    l=0
    while l<n:
        if a[l]==0:
            ptr=l
            while ptr<=n:
                a[ptr],a[ptr+1]=a[ptr+1],a[ptr]
                ptr+=1
        l+=1
    print(a)


a=[0,0,1]
# moveZero(a)
moveZeroInPlace(a)
