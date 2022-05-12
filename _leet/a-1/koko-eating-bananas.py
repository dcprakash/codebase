'''
https://leetcode.com/problems/koko-eating-bananas/solution/

If Koko can eat all the piles with a speed of nn, she can also finish the task with the speed of n + 1 (i.e., if eatinf 4 bananas work, then eating 5 bananas per hr will also work)
    With a larger eating speed, Koko will spend less or equal time on every pile. Thus, the overall time is guaranteed to be less than or equal to that of the speed nn
If Koko can't finish with a speed of nn, then she can't finish with the speed of n - 1n−1 either. 
    With a smaller eating speed, Koko will spend more or equal time on every pile, thus the overall time will be greater than or equal to that of the speed nn.

If the current speed is workable, the minimum workable speed should be on its left inclusively. 
If the current speed is not workable, that is, too slow to finish the eating task, then the minimum workable speed should be on its right exclusively.

Let the lower bound be 1, the minimum possible eating speed since there is no speed slower than 1. 
The upper bound will be the maximum eating speed, that is the maximum number of bananas in a pile.

binary search
apple
bananas
'''

from math import ceil

class Solution:
    def minEatingSpeed(self, piles, h):
        eat_bananna = lambda x : sum([ceil(n / x) for n in piles])
        d = 1
        while eat_bananna(d) > h:
            d += 1
        
        return d
    
    def minEatingSpeedEff(self, piles, h):  
        # Initalize the left and right boundaries     
        left = 1
        right = max(piles)
        
        while left < right:
            # Get the middle index between left and right boundary indexes.
            # hour_spent stands for the total hour Koko spends.
            middle = (left + right) // 2            
            hour_spent = 0
            
            # Iterate over the piles and calculate hour_spent.
            # We increase the hour_spent by ceil(pile / middle)
            for pile in piles:
                hour_spent += ceil(pile / middle)
            
            # Check if middle is a workable speed, and cut the search space by half.
            # we finished early, keep this as our tentative ans. Now reduce right so koko can eat slowly
            if hour_spent <= h:
                right = middle
            else:
                left = middle + 1
        
        # Once the left and right boundaries coincide, we find the target value,
        # that is, the minimum workable eating speed.
        return right
    
s=Solution()
print(s.minEatingSpeed([3,6,7,11],8))
print(s.minEatingSpeedEff([3,6,7,11],8))
