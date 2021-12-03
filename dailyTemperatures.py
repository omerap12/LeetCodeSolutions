answer to: https://leetcode.com/problems/daily-temperatures/
    
class Solution(object):
    def dailyTemperatures(self, temperatures):
        data_structure = {len(temperatures)-1: 0} # create dictionary for dynamic programming
        answer = [0] * len(temperatures)  # create first list of zeroes
        for i in range(len(temperatures) - 2, -1, -1): # start looping through the array from the end
            if temperatures[i] < temperatures[i + 1]: # if the current day temp is less than it's next day temp
                answer[i] = 1
                data_structure[i] = 1
            else:
                # if the current day temp is bigger than next day day temp
                self.helper(data_structure, i, temperatures, answer)
        return answer

    def helper(self, data, current_index, temperatures, answer):
        # check if is there bigger temp in the next days, if not than 0
        if data[current_index+1] == 0:
            data[current_index] = 0
            return
        above_index = data[current_index + 1] + 1 + current_index  # get the index of the next big temperature
        while True:
            if data[above_index] == 0: # if there is no hotter than 0
                data[current_index] = 0
                break
            if temperatures[current_index] < temperatures[above_index]: # if the next index day is warmer
                data[current_index] = above_index - current_index # add the index value to data
                answer[current_index] = data[current_index] # answer[i] = index of the next warmer day
                break
            else:
                # go to the next warmer day
                above_index = above_index+data[above_index]
