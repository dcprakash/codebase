'''
https://leetcode.com/problems/longest-consecutive-sequence/solution/

If the current number and the previous are equal, then our current sequence is neither extended nor broken, so we simply move on to the next number. 
If they are unequal, then we must check whether the current number extends the sequence (i.e. nums[i] == nums[i-1] + 1). 
    If it does, then we add to our current count and continue. 
Otherwise, the sequence is broken, so we record our current sequence and reset it to 1 (to include the number that broke the sequence). 
It is possible that the last element of nums is part of the longest sequence, so we return the maximum of the current sequence and the longest one.
sort and check gives O(nlgn)

we can use hashmap option to optimize it
the numbers are stored in a HashSet (or Set, in Python) to allow O(1)O(1) lookups
we only attempt to build sequences from numbers that are not already part of a longer sequence
This is accomplished by first ensuring that the number that would immediately precede the current number in a sequence is not present, 
    as that number would necessarily be part of a longer sequence.
'''


class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)
    

    def longestConsecutiveEff(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

