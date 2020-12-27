
"""
https://leetcode.com/problems/word-ladder/submissions/
"""

from collections import defaultdict, deque


def WordLadder(beginWord, endWord, wordList):
    # create new dict of all the words in wordlist, with one escaped char
    adj = defaultdict(list)
    for word in wordList:
        for i in range(len(word)):
            adj[word[:i] + '_' + word[i+1:]].append(word)
    
    # each time a word is counted, add to visited to avoid duplicate word checking
    visited = set()
    
    q = deque([(beginWord, 1)])
    while q:
        word, k = q.popleft()
    
        if word == endWord:
            return k
    
        if word not in visited:
            visited.add(word)
            for i in range(len(word)):
                neighbors = word[:i] + '_' + word[i+1:]
                for neighbor in adj[neighbors]:
                    q.append((neighbor, k+1))
    
    return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(WordLadder(beginWord, endWord, wordList))
