"""
https://leetcode.com/problems/design-hit-counter/
"""

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time=[0]*300
        self.count=[0]*300
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        # if timestamp=400, then i=100
        # at index 100, we store value 400 and count=1 to indicate 400 occured for first time
        # if timestamp=400 comes again, then at 100 we already have 400, just increase the count
        i=timestamp%300
        if self.time[i]!=timestamp:
            self.time[i]=timestamp
            self.count[i]=1
        else:
            self.count[i]+=1
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        # number of hits is stored in counts, so for last 5min, 300sec
        # add number hits from count to ans if time less than 300sec
        # from 0 to 300, if all self.time values are b.w 0 and 300,
        # all hits came within 300sec i.e., 5min
        print(self.time)
        print(self.count)
        ans=0
        for i in range(300):
            #
            if self.time[i]>timestamp-300:  # refer below for explaination
                ans+=self.count[i]
        return ans
        


hitCounter = HitCounter()
hitCounter.hit(1)       # hit at timestamp 1.
hitCounter.hit(2)       # hit at timestamp 2.
hitCounter.hit(3)       # hit at timestamp 3.
# hitCounter.getHits(4)   # get hits at timestamp 4, return 3.
hitCounter.hit(300)     # hit at timestamp 300.
hitCounter.getHits(300) # get hits at timestamp 300, return 4.
hitCounter.getHits(301) # get hits at timestamp 301, return 3.


'''
Input
["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
[[], [1], [2], [3], [4], [300], [300], [301]]
Output
[null, null, null, null, 3, null, 4, 3]

Explanation
HitCounter hitCounter = new HitCounter();
hitCounter.hit(1);       // hit at timestamp 1.
hitCounter.hit(2);       // hit at timestamp 2.
hitCounter.hit(3);       // hit at timestamp 3.
hitCounter.getHits(4);   // get hits at timestamp 4, return 3.
hitCounter.hit(300);     // hit at timestamp 300.
hitCounter.getHits(300); // get hits at timestamp 300, return 4.


if self.time[i]>timestamp-300: is required to address this scenario
hitCounter.getHits(301); // get hits at timestamp 301, return 3.  

when we stored timestamp=1, it was at 1%300 i.e., at timestamp[1]=1
    301-300=1 so we dont include this

'''
