"""
Your module description
"""

l=[0, 1, 0, 2, 0,-1,-1, 0, 0,-1]
ans=l[0]
for i in range(1,len(l)):
    l[i]=l[i]-l[i-1]
    ans=max(ans,l[i])
print(ans)
