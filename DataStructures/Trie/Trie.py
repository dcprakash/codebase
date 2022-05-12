# https://medium.com/@info.gildacademy/a-simpler-way-to-implement-trie-data-structure-in-python-efa6a958a4f2
# https://leetcode.com/problems/implement-trie-prefix-tree/


'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings.

'''

from collections import defaultdict


class TrieNode():
    def __init__(self):
        self.children = defaultdict()
        self.terminating = False


class Trie():
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def insert(self, word):
        root = self.root
        for i in range(len(word)):
            if word[i] not in root.children:
                root.children[word[i]] = self.get_node()
            root = root.children.get(word[i])
        root.terminating = True


    def search(self, word):
        root = self.root
        for i in range(len(word)):
            if not root:
                return False
            root = root.children.get(word[i])
        return True if root and root.terminating else False


    def delete(self, word):
        root = self.root
        for i in range(len(word)):
            if not root:
                print ("Word not found")
                return -1
            root = root.children.get(word[i])

        if not root:
            print ("Word not found")
            return -1
        else:
            root.terminating = False
            return 0

    def update(self, old_word, new_word):
        val = self.delete(old_word)
        if val == 0:
            self.insert(new_word)

    

if __name__ == "__main__":
    # strings = ["pqrs", "pprt", "psst", "qqrs", "pqrs"]
    strings = ["pqrs", "qqrs", "pqrs", "pprt"]

    t = Trie()
    for word in strings:
        t.insert(word)

    print(t.search("pqrs"))
    print(t.search("pprt"))

    t.delete("pprt")

    print(t.search("pprt"))

    t.update("mnop", "pprt")