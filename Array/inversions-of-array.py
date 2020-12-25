# https://www.geeksforgeeks.org/counting-inversions/

a=[8, 4, 2, 1]
n=len(a)
count=0
for i in range(n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            print(a[i],a[j])
            count+=1
print("Number of inversions = {}".format(count))