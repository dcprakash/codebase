s="01101"
n=len(s)
count=0
for i in range(n):
    if s[i]=="1":
        for j in range(i+1,n):
            if s[j]=="1":
                count+=1
            else:
                continue
print(count)