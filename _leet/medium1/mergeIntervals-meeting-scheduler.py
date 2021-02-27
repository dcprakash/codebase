'''
https://leetcode.com/problems/meeting-scheduler/
'''
# https://leetcode.com/problems/interval-list-intersections/submissions/
# Merge Intervals of list intersections
# interval-list-intersections


def minAvailableDuration(firstList, secondList, duration):
    i=j=0
    fn=len(firstList)
    sn=len(secondList)
    firstList.sort()
    secondList.sort()
    
    while i<fn and j<sn:
        lo=max(firstList[i][0],secondList[j][0])
        hi=min(firstList[i][1],secondList[j][1])
        if hi-lo>=duration:
            # res.append((lo,lo+duration))
            return [lo,lo+duration]        
        if firstList[i][1] < secondList[j][1]:
            i+=1
        else:
            j+=1
    
    return []


firstList = [[10,50],[60,120],[140,210]]
secondList = [[0,15],[60,70]]
duration=8
print(minAvailableDuration(firstList, secondList, duration))
