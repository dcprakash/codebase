

def findTripSum(a,n,x):
    a.sort()
    for i in range(n):
        l=i+1
        r=n-1
        while l<r:
            if a[i]+a[l]+a[r]==x:
                print(a[i],a[l],a[r],x)
                l+-1
                r-=1
            elif a[i]+a[l]+a[r] < x:
                l+-1
            else:
                r-=1


a=[1,4,3,2,6]
n=len(a)
x=6
findTripSum(a,n,x)