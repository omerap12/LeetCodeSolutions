solution to: https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
        
class Solution(object):
    def groupThePeople(self, groupSizes):
        answer = []
        data_table = {} # value : [all indexes with the value]
        # iterating through the list, and entering data to the dataTable
        for i in range(len(groupSizes)):
            if groupSizes[i] not in data_table.keys():
                data_table[groupSizes[i]] = [i]
            else:
                data_table[groupSizes[i]].append(i)
        # iterating through the data table and cut the list according to key value
        for key, value in data_table.items():
            start_index = 0
            stop_index = len(value)
            # cutting lists
            for i in range(start_index, stop_index, key):
                start_index = i
                answer.append(value[start_index:start_index+key])
        return answer
