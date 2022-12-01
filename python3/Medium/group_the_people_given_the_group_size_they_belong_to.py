# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/

class Solution:
    def groupThePeople(self, groupSizes):
        res = []
        dict_people = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] in dict_people.keys():
                dict_people[groupSizes[i]].append(i)
            else:
                dict_people[groupSizes[i]] = [i]
            if len(dict_people[groupSizes[i]]) == groupSizes[i]:
                res.append(dict_people[groupSizes[i]].copy())
                dict_people[groupSizes[i]] = []
        return res

n = Solution()
groupSizes = [3,3,3,3,3,1,3]
print(n.groupThePeople(groupSizes))