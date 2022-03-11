"""
https://leetcode.com/problems/design-a-leaderboard/

"""
class Leaderboard:

    def __init__(self):
        self.scores={}
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId]=0
        self.scores[playerId]+=score

        
    def top(self, K: int) -> int:
        res=[]
        for x in self.scores.values():
            bisect.insort(res, x)
            if len(res)>K:  res.pop(0)
        return sum(res)
        

    def reset(self, playerId: int) -> None:
        self.scores[playerId]=0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)

'''
bisect(list, num, beg, end) :- This function returns the position in the sorted list, where the number passed in argument can be placed so as to maintain the resultant list in sorted order.
bisect_left(list, num, beg, end) :- This function returns the position in the sorted list, where the number passed in argument can be placed so as to maintain the resultant list in sorted order. If the element is already present in the list, the left most position where element has to be inserted is returned.
bisect_right(list, num, beg, end)
insort(list, num, beg, end) :- This function returns the sorted list after inserting number in appropriate position, if the element is already present in the list, the element is inserted at the rightmost possible position.
insort_left(list, num, beg, end) 
'''