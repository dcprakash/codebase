str1 = "alphabets"
str2 = "characters"
str3=""
for i in str1:
    if i not in str2 and i not in str3:
        str3+=i
for i in str2:
    if i not in str1 and i not in str3:
        str3+=i
print(str3)