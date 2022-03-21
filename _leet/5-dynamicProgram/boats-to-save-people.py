'''
https://leetcode.com/problems/boats-to-save-people/

boat save people
If the heaviest person can share a boat with the lightest person, 
    then do so. Otherwise, the heaviest person can't pair with anyone, 
    so they get their own boat.
note: its assumed that boat is big enough to fit atleast one person
'''


class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()   #[1,2,2,3]
        i=0
        j=len(people)-1
        ans=0
        while i<=j:
            ans+=1
            if people[i]+people[j]<=limit:
                i+=1
            j-=1
        return ans


people = [3,2,2,1]
limit = 3    
s=Solution()
print(s.numRescueBoats(people, limit))