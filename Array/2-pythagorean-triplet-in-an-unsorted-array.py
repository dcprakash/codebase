# https://www.geeksforgeeks.org/find-pythagorean-triplet-in-an-unsorted-array/


def pythagoreanTriplet(a,n):
    pya=[]
    for i in range(n):
        pya.append(a[i]*a[i])
    pya.sort()
    # print(pya)  #[1, 9, 16, 25, 36]
    
    # for i in reversed(range(2,n)):
    for i in range(n-1,2,-1):   #i=4,3,2
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