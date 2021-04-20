'''
https://leetcode.com/problems/shortest-word-distance-ii/solution/

words can occur at multiple locations. If we have K occurrences for the word1 and L occurrences for the word2, 
then iteratively checking every pair of indices will give us a O(N^2)  algorithm which won't be optimal at all.

word1_locations = [2,4,5,9]
word2_locations = [4,10,11]

i, j = 0, 0
min_diff = 2 (abs(2 - 4))
word1[i] < word2[j] i.e. 2 < 4
  move i one step forward

i, j = 1, 0 (abs(4 - 4))
min_diff = 0 (We hit the jackpot!)  


'''

from collections import defaultdict
class WordDistance:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.locations = defaultdict(list)

        # Prepare a mapping from a word to all it's locations (indices).
        for i, w in enumerate(words):
            self.locations[w].append(i)
        print(self.locations)
        # {'practice': [0], 'makes': [1, 4], 'perfect': [2], 'coding': [3]})


    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        loc1, loc2 = self.locations[word1], self.locations[word2]
        l1, l2 = 0, 0
        min_diff = float("inf")

        # Until the shorter of the two lists is processed
        while l1 < len(loc1) and l2 < len(loc2):
            min_diff = min(min_diff, abs(loc1[l1] - loc2[l2]))
            if loc1[l1] < loc2[l2]:
                l1 += 1
            else:
                l2 += 1
        return min_diff


sol=WordDistance(["practice","makes","perfect","coding","makes"])
# print(sol.shortest("coding","practice"))
print(sol.shortest("makes","coding"))
