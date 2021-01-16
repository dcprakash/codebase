# https://leetcode.com/problems/task-scheduler/solution/
# idle time between tasks


class Solution(object):
    def leastInterval(self, tasks, n):
        frequencies = 26*[0]
        for t in tasks:
            frequencies[ord(t)-ord('A')]+=1
        frequencies.sort()
        # print(frequencies)
        
        f_max=frequencies.pop()
        idle_time = (f_max-1)*n
        
        while frequencies and idle_time>0:
            idle_time-=min(f_max-1, frequencies.pop())
        idle_time=max(0,idle_time)
        
        return len(tasks) + idle_time


# tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
tasks = ["A","A","A","B","B","B"]
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