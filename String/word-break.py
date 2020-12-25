# https://www.geeksforgeeks.org/word-break-problem-dp-32/



# def wordBreak(wordList,word):
# 	n=len(word)
# 	for i in range(1,n+1):
# 		if any((word[:i] in wordList) and wordBreak(wordList, word[i:])):
# 			return True
# 	return False
	
def wordBreak(wordList, word): 
	if word == '': 
		return True
	else: 
		wordLen = len(word) 
		return any([(word[:i] in wordList) and wordBreak(wordList, word[i:]) for i in range(1, wordLen+1)]) 



wordList=["i", "like", "sam", "sung", "samsung", "mobile"]
word="ilike"
if wordBreak(wordList,word):
	print("Word exist")
else:
	print("Cannot find word in dictionary")


