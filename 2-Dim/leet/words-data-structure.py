# https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Design workd dictionary
# trie for word dictionary
'''
https://leetcode.com/explore/interview/card/google/62/recursion-4/462/
word-search-board.py
word search board
'''


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie

        for ch in word:
            if not ch in node:
                node[ch] = {}
            node = node[ch]
        node['$'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any letter.
        """
        print(self.trie)
        def search_in_node(word, node) -> bool:
            for i, ch in enumerate(word):
                if not ch in node:
                    # if the current character is '.'
                    # check all possible nodes at this level
                    if ch == '.':
                        for x in node:  #try all possible paths bcz of .
                            if x != '$' and search_in_node(word[i + 1:], node[x]):
                                return True
                    # if no nodes lead to answer
                    # or the current character != '.'
                    return False
                # if the character is found
                # go down to the next level in trie
                else:
                    node = node[ch]
            return '$' in node

        return search_in_node(word, self.trie)


wordDictionary = WordDictionary();
wordDictionary.addWord("bag")
wordDictionary.addWord("dad")
wordDictionary.addWord("bab")   # {'b': {'a': {'g': {'$': True}, 'b': {'$': True}}}, 'd': {'a': {'d': {'$': True}}}}
wordDictionary.search(".ag")
# {'b': {'a': {'g': {'$': True}}}, 'd': {'a': {'d': {'$': True}}}}
