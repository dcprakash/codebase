# https://leetcode.com/problems/find-duplicate-file-in-system/
# duplicate contents in files

from collections import defaultdict

def findDuplicate(paths):
    maps = defaultdict(list)
    for path in paths:
        path,*files=path.split(' ')
        for file in files:
            file, content=file.split("(")
            maps[content].append(path+'/'+file)
    return [i for i in maps.values()]


paths=["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
# paths=["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]
print(findDuplicate(paths))