# https://leetcode.com/problems/minimum-time-difference/

# convert string to int and to minutes, sort the list
# start checking diff b.w negihbours; keep track latest minimum


def findMinDifference(timePoints):
    """
    :type timePoints: List[str]
    :rtype: int
    """
    timePoints, m = sorted(map(lambda s: int(s[:2])*60 + int(s[3:]), timePoints)), float('inf')
    for i in range(1, len(timePoints)):
        if timePoints[i] - timePoints[i-1] < m:
        	m = timePoints[i] - timePoints[i-1]
    return min(m, 1440 - timePoints[-1] + timePoints[0])
    
timePoints = ["23:59","02:00","01:30"]	# (23*60)+59=1439 #[90, 120, 1439]
print(findMinDifference(timePoints))