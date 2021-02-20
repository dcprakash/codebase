# https://leetcode.com/problems/task-scheduler/solution/
# idle i.e., cool down period time between two SAME tasks
# Number of busy slots is defined by the number of tasks to execute: len(tasks)
# idle slots = frequency of most frequent task: idle_time <= (f_max - 1) * n.
# f_max=5 bcz of A
# idle_time=5-1*2=8 bcz     A--A--A--A--A
# to schedule B -> 8-2=6    AB-AB-A--A--A
# to schedule C -> 6-1=5    ABCAB-A--A--A   idle slots = 5
# number of tasks = len(tasks)  = 8
# 8+5=13

class Solution(object):
    def leastInterval(self, tasks, n):
        frequencies = 26*[0]
        for t in tasks:
            frequencies[ord(t)-ord('A')]+=1 #ord() returns integer representing Unicode character.
        frequencies.sort()  # [0,.., 0, 1, 2, 5]
        # print(frequencies)
        
        f_max=frequencies.pop()
        idle_time = (f_max-1)*n
        
        while frequencies and idle_time>0:
            idle_time-=min(f_max-1, frequencies.pop())
        # idle_time=max(0,idle_time)
        
        return len(tasks) + idle_time


tasks = ["A","B","A","A","B","C","A","A"]
n = 2
s=Solution()
print(s.leastInterval(tasks, n))


'''
The maximum number of tasks is 26. Let's allocate an array frequencies of 26 elements to keep the frequency of each task.

Iterate over the input array and store the frequency of task A at index 0, the frequency of task B at index 1, etc.

Sort the array and retrieve the maximum frequency f_max. This frequency defines the max possible idle time: idle_time = (f_max - 1) * n.

Pick the elements in the descending order one by one. At each step, decrease the idle time by min(f_max - 1, f) where f is a current frequency. Remember, that idle_time is greater or equal to 0.

Return busy slots + idle slots: len(tasks) + idle_time.
'''