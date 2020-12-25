# https://practice.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1

a = [16,17,4,3,5,2] 
n = len(a) 

msf=float('-inf')
res=[]
for i in range(n-1, -1, -1):
    msf=max(msf,a[i])
    if a[i]>=msf:
        res.append(a[i])
print("Leaders in array are {}".format(res))
    
    