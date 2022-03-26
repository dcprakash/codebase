
n = "hate love peace love peace hate love peace love peace peace"

print("*******method1*******")
n = n.split(" ")
d = {}
for e in n:
    if e in d:
        d[e] = d[e]+1
    else:
        d[e]=1

for i in d.items():
    if i[1] == 2:
        print(i[0])

# print("*******method2*******")
# import collections
# word_counts = collections.Counter(n)
# print word_counts
# for word, count in sorted(word_counts.items()):
#     print("{} : {}".format(word, count))

 