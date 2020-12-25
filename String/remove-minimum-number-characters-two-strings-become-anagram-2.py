# https://www.geeksforgeeks.org/remove-minimum-number-characters-two-strings-become-anagram/

str1 = "bcadeh"
str2 = "hea"
temp=""
remove=""
count=0
for i in str1:
    if i in str2:
      temp+=i
    else:
        remove+=i
        count+=1
print("Removed {} characters {}".format(count,remove))
print("{} and {} are anagram".format(str2, temp))
