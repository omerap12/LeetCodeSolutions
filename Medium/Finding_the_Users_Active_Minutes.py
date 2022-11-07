Solution To: https://leetcode.com/problems/finding-the-users-active-minutes/

class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        answer = [0] * k  # create list of the answer, default value is 0
        hash_map = {}  # {user_id: [list of action numbers]}
        for log in logs:  # iterating through the logs
            if log[0] in hash_map.keys():  # if log[0] (means user ID) already in map
                if log[1] in hash_map[log[0]]:  # if user action already in list of actions, don't count it
                    continue
                hash_map[log[0]].append(log[1])  # add user action index to the list
            else:
                hash_map[log[0]] = [log[1]]  # add new user id with list of one action

        for key, value in hash_map.items():  # iterating through the map and calculate answer
            answer[len(value) - 1] += 1
        return answer
