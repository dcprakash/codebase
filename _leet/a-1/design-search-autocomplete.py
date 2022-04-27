'''
https://leetcode.com/problems/design-search-autocomplete-system/
    https://leetcode.com/explore/featured/card/google/65/design-4/3095/
    
https://www.youtube.com/watch?v=9qC-8NdHtwM

using trie and minheap
    https://leetcode.com/problems/design-search-autocomplete-system/discuss/1853893/Python-min-heap-and-trie-solution
    
'''

from collections import defaultdict


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.search=''
        self.history=defaultdict(int)
        for i in range(len(sentences)):
            self.history[sentences[i]]=times[i]
        # print(self.history) # defaultdict(<class 'int'>, {'i love you': 5, 'island': 3, 'iroman': 2, 'i love leetcode': 2})
        self.matches=[]


    def input(self, c: str) -> List[str]:
        if c=='#':
            self.history[self.search]+=1
            self.search=''
            self.matches=[]
            return
        
        if not self.search:
            for sentence in self.history:
                if sentence[0]==c:
                    self.matches.append([sentence, self.history[sentence]])
            self.matches.sort(key=lambda x: (-x[1],x[0]))
            self.matches=[x[0] for x in self.matches]
        else:
            i=len(self.search)
            self.matches=[match for match in self.matches if len(match)>i and match[i]==c]
        self.search+=c
        return self.matches[:3]        


obj = AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]);
print(obj.input("i")) # return ["i love you", "island", "i love leetcode"]. There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.
print(obj.input(" ")) # return ["i love you", "i love leetcode"]. There are only two sentences that have prefix "i ".
print(obj.input("a")) # return []. There are no sentences that have prefix "i a".
print(obj.input("#")) # return []. The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.
