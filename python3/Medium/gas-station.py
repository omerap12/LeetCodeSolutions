solution To:https://leetcode.com/problems/gas-station/

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        first_jump_possible = [0] * len(gas)  # initiate list for the first gas stations
        for i in range(len(gas)):
            if gas[i] == 0:  # if gas station value is 0 means we can't start there, put -1
                first_jump_possible[i] = -1
                continue
            first_jump_possible[i] = gas[i] - cost[i]  # put the value of the gas staion - cost of the gas station

        for j in range(len(first_jump_possible)):  # checking where to start
            if first_jump_possible[j] < 0:  # if gas station value is less than 0 means we can't start there
                continue
            if self.one_time_solver(gas, cost, j, gas[j]) != -1:  # call function to check validity,return index if true
                return j
        return -1

    # aux function to check validity from specific gas station spot
    def one_time_solver(self, gas, cost, index_start, start_gas):
        stop_index = index_start
        first_time = True
        current_gas = start_gas
        while stop_index != index_start or first_time:  # start loop iteration
            if index_start + 1 == len(gas):  # if were on the last index of the list
                if current_gas - cost[index_start] < 0:  # if there is no more gas available
                    return -1
                current_gas = current_gas - cost[index_start] + gas[0]  # calculate current gas
                index_start = 0  # index is set to 0, start from index 0 on list
                first_time = False
                continue
            if current_gas - cost[index_start] < 0:  # if there is no more gas available
                return -1
            current_gas = current_gas - cost[index_start] + gas[index_start + 1]  # calculate current gas
            first_time = False
            index_start += 1  # index is up by one
