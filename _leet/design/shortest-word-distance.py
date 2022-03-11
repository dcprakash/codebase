'''
https://leetcode.com/problems/shortest-word-distance-ii/solution/

When the problem talks about the distance between two words, 
    it essentially means the absolute gap between the indices of the two words in the list. 
    For e.g. if the first word occurs at a location i and the second word occurs at the location j, 
    then the distance between the two would be abs(i - j).


words can occur at multiple locations. If we have K occurrences for the word1 and L occurrences for the word2, 
then iteratively checking every pair of indices will give us a O(N^2)  algorithm which won't be optimal at all.

The idea is to use a two pointer approach. 
Let's say we have a pointer i for the sorted list of indices of word1 and j for the sorted list of indices of word2. 
At every iteration, we record the difference of indices i.e. abs(word1[i] - word2[j]). 
Once we've done that, we have two possible choices for progressing the two pointers.

    word1[i] < word2[j]
    If this is the case, that means there is no point in moving the j pointer forward. 
    The location indices for the words are in a sorted order. We know that word2[j + 1] > word2[j] because these indices are sorted. 
    So, if we move j forward, then the difference abs(word1[i] - word2[j + 1]) would be even greater than abs(word1[i] - word2[j]). 
    That doesn't help us since we want to find the minimum possible distance (difference) overall.
    
    So, if we have (word1[i] < word2[j]), we move the pointer 'i' one step forward i.e. (i + 1) in the hopes that 
    abs(word1[i + 1] - word2[j]) would give us a lower distance than abs(word1[i] - word2[j])
    

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
        # Since we process all the words from left to right, we will get all the indices in a sorted order by default for all the words. 
        # So, we don't have to sort the indices ourselves.
        
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
