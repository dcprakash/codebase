# https://leetcode.com/problems/string-compression/

# def compress(chars):
#     anchor = write = 0
#     for read, c in enumerate(chars):
#         if read + 1 == len(chars) or chars[read + 1] != c:
#             chars[write] = chars[anchor]
#             write += 1
#             if read > anchor:
#                 for digit in str(read - anchor + 1):
#                     chars[write] = digit
#                     write += 1
#             anchor = read + 1
#     return write


chars = ["a","a","b","b","c","c","c"]
# print(compress(chars))

d={}
for i in chars:
    if i in d:  d[i]+=1
    else:   d[i]=1
res=[]
for k,v in sorted(d.items()):
    res.append(k)
    res.append(str(v))
print(res)


    
    