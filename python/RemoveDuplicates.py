words = "geeksforgeeks"
newWord = ""
for i in words:
    if i not in newWord:
        newWord = newWord + i
print newWord
print len(newWord)