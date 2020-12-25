arr = [900, 940, 950, 1100, 1500, 1800] 
dep = [910, 1200, 1120, 1130, 1900, 2000] 
arr.sort()
dep.sort()
res=0
for i in range(len(arr)-1):
    p=0
    if arr[i+1]<dep[i]:
        p+=1
        if p>res:
            res=p
    else:
        p=0
print(res)
        