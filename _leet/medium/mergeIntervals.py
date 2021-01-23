"""
https://leetcode.com/problems/merge-intervals
merge intervals of list
"""


def mergeIntervals(intervals, n):
    intervals.sort(key=lambda x: x[0])
    # print(intervals)  # [[1, 3], [2, 6], [8, 10], [15, 18]]
    
    merged=[]
    for item in intervals:
        # merged not empty
        # merged last item's second element is less than item's second element
        # print(merged[-1][1])  # gives last item in list
        if not merged or merged[-1][1] < item[0]:
            merged.append(item)
        else:
            merged[-1][1]=max(merged[-1][1],item[1])
    
    return merged   

intervals = [[2,6],[1,3],[8,10],[15,18]]

print(mergeIntervals(intervals,len(intervals)))

        
    
