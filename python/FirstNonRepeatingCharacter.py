s = "hello"
l = []
dic = {}
for i in s:
    if i not in l:
        l.append(i)
        dic.update({i:1})
    else:
        dic[i] += 1
flag = 0
for i in l:
    if(dic[i] == 1):
        flag = 1
        print(i)
        break
if(flag == 0):
    print(-1)