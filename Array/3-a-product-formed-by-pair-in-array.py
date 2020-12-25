# https://www.geeksforgeeks.org/pair-with-given-product-set-1-find-if-any-pair-exists/

def findProdKeyPair(a,n,x):
    a.sort()
    l=0
    r=n-1
    while l<r:
        if a[l]*a[r]==x:
            print(a[l],a[r])
            l+=1
            r-=1
        if a[l]*a[r]<x:
            l+=1
        elif a[l]*a[r]>x:
            r+=1


a = [10, 20, 9, 40] 
x = 400
findProdKeyPair(a,len(a),x)
