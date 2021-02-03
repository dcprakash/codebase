'''
lists pairs are disjoint i.e., no 2 intervals are same in list
lsits are already sorted
https://www.youtube.com/watch?v=Qh8ZjL1RpLI&ab_channel=TECHDOSE
'''
# https://leetcode.com/problems/interval-list-intersections/submissions/
# Merge Intervals of list intersections
# interval-list-intersections


def intervalIntersection(firstList, secondList):
    res=[]
    i=j=0
    fn=len(firstList)
    sn=len(secondList)
    
    while i<fn and j<sn:
        lo=max(firstList[i][0],secondList[j][0])
        hi=min(firstList[i][1],secondList[j][1])
        if lo <= hi:
            res.append((lo,hi))
        
        if firstList[i][1] < secondList[j][1]:
            i+=1
        else:
            j+=1
    
    return res


firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
print(intervalIntersection(firstList, secondList))
