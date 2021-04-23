"""
https://leetcode.com/problems/angle-between-hands-of-a-clock/solution/

minute handle
    whole circle is 360deg or 60min; 360/60=6 so 1min=6deg
    5min=5*6=30deg;     50min=50*6=300deg
hour handle
    whole circle is 360deg or 12hr; 360/12=30 so 1hr=30deg
    12hr=360deg but this should be 0deg hence, (hour mod 12)*30
    
    when minutes>0, consider minutes for hour handle moment
        hour_angle = (hour % 12 + minutes / 60)

hour 3*30=90
    but hour handle has moved a bit, (3+(30/60))*30=105
minute 30*6=180


"""


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        one_min_angle = 6
        one_hour_angle = 30
        
        minutes_angle = one_min_angle * minutes
        hour_angle = (hour % 12 + minutes / 60) * one_hour_angle
        
        diff = abs(hour_angle - minutes_angle)
        return min(diff, 360 - diff)
        
s=Solution()
print(s.angleClock(3, 30))


