'''
https://leetcode.com/problems/word-squares/solution/
https://leetcode.com/explore/interview/card/google/62/recursion-4/370/

[
"b a l l",
"a r e a",
"l e a d",
"l a d y"
]

As we can see from the definition, for a word square with equal-sized row and column, 
    the resulting letter matrix should be symmetrical across its diagonal.




The idea is that we construct the word square row by row from top to bottom. 
At each row, we simply do trial and error, i.e. we try with one word, 
    if it does not meet the constraint then we try another one.

'''

class Solution:

    def wordSquares(self, words):

        self.words = words
        self.N = len(words[0])

        results = []
        word_squares = []
        for word in words:
            # try with every word as the starting word
            word_squares = [word]
            self.backtracking(1, word_squares, results)
        return results

    def backtracking(self, step, word_squares, results):

        if step == self.N:
            results.append(word_squares[:])
            return

        prefix = ''.join([word[step] for word in word_squares])
        # find out all words that start with the given prefix        
        for candidate in self.getWordsWithPrefix(prefix):
            # iterate row by row
            word_squares.append(candidate)
            self.backtracking(step+1, word_squares, results)
            word_squares.pop()

    def getWordsWithPrefix(self, prefix):
        for word in self.words:
            if word.startswith(prefix):
                yield word
                

words=["area","ball","lead","lady"]
# words=['able', 'area', 'lead', 'lady', 'ball']
# words=['ball', 'able', 'area', 'lead', 'lady']

s=Solution()
print(s.wordSquares(words))