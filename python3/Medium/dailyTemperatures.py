#https://leetcode.com/problems/daily-temperatures/
    
class Solution(object):
    def dailyTemperatures(self, temperatures):
        data_structure = {len(temperatures)-1: 0} # create data for dynamic programming
        answer = [0] * len(temperatures)  # create first list of zeroes
        for i in range(len(temperatures) - 2, -1, -1): # start loop from the end
            if temperatures[i] < temperatures[i + 1]: # if the next day is warmer, put 1 in data & answer
                answer[i] = 1
                data_structure[i] = 1
            else:
                # calculate the next warmer day index function
                self.helper(data_structure, i, temperatures, answer)
        return answer

    def helper(self, data, current_index, temperatures, answer):
        # if there is not warmer day
        if data[current_index+1] == 0:
            data[current_index] = 0
            return
        check = False
        # get the index of the next warmer day from the data
        above_index = data[current_index + 1] + 1 + current_index  # get the index of the next big temperature
        while not check:
            # if there is no warmer day
            if data[above_index] == 0:
                data[current_index] = 0
                check = True
            # if its warmer day indeed
            if temperatures[current_index] < temperatures[above_index]:
                # put the distance from the current day in data and answer
                data[current_index] = above_index - current_index
                answer[current_index] = data[current_index]
                check = True
            else:
                # get the next warmer day
                above_index = above_index+data[above_index]
