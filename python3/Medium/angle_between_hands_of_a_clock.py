# https://leetcode.com/problems/angle-between-hands-of-a-clock/description/
class Solution:
    def angleClock(self, hour, minutes):
        """
        A clock is a circle, and a circle always contains 360 degrees.
        Since there are 60 minutes on a clock, each minute mark is 6 degrees.
        Since there are 12 hours on the clock, each hour mark is 30 degrees.
        hour_hand_angle = (hour + minutes/60)*60
        minute_hand_angle = minute*6
        angle = abs(hour_hand_angle-minute_hand_angle)
        return min(360-angle,angle) -> calculate the right degree
        """
        hour_hand_angle = (360/12)*hour + minutes/60*30
        minutes_hand_angle = 360/60*minutes
        res = hour_hand_angle - minutes_hand_angle
        if res < 0:
            res = -res
        res = min(360-res,res)
        return res
