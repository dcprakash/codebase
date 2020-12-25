n = [8, 4, 4, 8, 23]
d = {}
for i in n:
    if i in d:
        d[i] = d[i]+1
    else:
        d[i] = 1
for key, value in d.items():
    if value%2!=0:
        print key
        print value