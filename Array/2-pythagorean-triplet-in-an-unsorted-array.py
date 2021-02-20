

def pythagoreanTriplet(a,n):
    pya=[]
    for i in range(n):
        pya.append(a[i]*a[i])
    pya.sort()
    
    for i in reversed(range(2,n)):
        l=0
        r=i-1
        while(l<r):
            if pya[l]+pya[r]==pya[i]:
                print(pya[l],pya[r],pya[i])
            if pya[l]+pya[r]<pya[i]:
                l+=1
            else:
                r-=1



a =[3, 1, 4, 6, 5]
n=len(a)
pythagoreanTriplet(a,n)