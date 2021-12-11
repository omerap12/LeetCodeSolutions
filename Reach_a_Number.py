Solutuon To: https://leetcode.com/problems/reach-a-number/

class Solution(object):
    def reachNumber(self, target):
        """
        observation: when calculating s = (1+2+...+n) if s>target than need to back a step so for some index i we 
        need to subtract -2i from s, so for every iteration when current_loaction (s) if current_loctaion> target and 
        (current_location - target)%2 == 0 return number of steps 
        :param target: the value to get 
        :return: minimum number of steps
        """

        if target == 0:
            return 0
        abs_target = abs(target)  # for cases when target is negative
        current_location = 0
        jump_counter = 0

        while True:
            jump_counter += 1
            current_location += jump_counter  # jump according to question (1+2+3+... etc)
            if current_location == abs_target:  # if were at the target return number of steps
                return jump_counter
            if current_location > abs_target and (
                    current_location - abs_target) % 2 == 0:  # observation for explanation
                return jump_counter
