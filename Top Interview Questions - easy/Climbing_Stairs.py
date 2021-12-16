Solution To: https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/569/

class Solution(object):
    def climbStairs(self, n):
        dynamic_array = [0] * n # creating array sizeof n 
        for i in range(n):
            if i == 0:
                dynamic_array[i] = 1 # one way to get to first floor
            elif i == 1:
                dynamic_array[i] = 2 # two ways to get to second floor
            else:
                dynamic_array[i] = dynamic_array[i - 1] + dynamic_array[i - 2] # number of ways to get to the i'th floor is the number of ways to get to the i-1 floor + number of ways to get to the i-2 floor
        return dynamic_array[n-1]
