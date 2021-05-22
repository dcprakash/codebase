# https://leetcode.com/problems/string-compression
# modify list of characters in place
# list compression

def compressEff(chars):
    anchor = write = 0
    for read, c in enumerate(chars):
        # if reached end or next char is not duplicate
        if read + 1 == len(chars) or chars[read + 1] != c:
            chars[write] = chars[read]
            write += 1
            if read > anchor:
                for digit in str(read - anchor + 1):
                    chars[write] = digit
                    write += 1
            anchor = read + 1
    return write


def compress(chars):
    d={}
    for i in chars:
        if i in d:  d[i]+=1
        else:   d[i]=1
    res=[]
    for k,v in sorted(d.items()):
        res.append(k)
        res.append(str(v))
    return len(res)
    

print(compressEff(["a","b","b","c","c"]))
print(compress(["a","a","b","b","c","c","c"]))

    
    