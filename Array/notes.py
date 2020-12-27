

def minJump(arr):
    area=0
    i=0
    n=len(arr)
    res=[]
    while i<n:
        res.append(arr[i])
        for j in range(arr[i]-1):
            i+=1
    if i==n-1:
        return res
    else:
        return 0

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(minJump(arr))
