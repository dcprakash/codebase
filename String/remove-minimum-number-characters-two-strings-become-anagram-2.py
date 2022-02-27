# https://www.geeksforgeeks.org/remove-minimum-number-characters-two-strings-become-anagram/
'''
Given two strings in lowercase, the task is to make them anagram. 
The only allowed operation is to remove a character from any string. 
Find minimum number of characters to be deleted to make both the strings anagram? 
If two strings contains same data set in any order then strings are called Anagrams. 
'''


def makeAnagram(a, b):
	buffer = [0] * 26
	for char in a:
		buffer[ord(char) - ord('a')] += 1
	for char in b:
		buffer[ord(char) - ord('a')] -= 1
	return sum(map(abs, buffer))


if __name__ == "__main__" :
	str1 = "bcadeh"
	str2 = "hea"
	print(makeAnagram(str1, str2))


'''
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
'''