class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        res = 0
        neighbors = {}
        for i in range(len(ages)):
            for j in range(len(ages)):
                if i == j or ages[j] <= 0.5 * ages[i] + 7 or ages[j] > ages[i] or (ages[j] > 100 and ages[i] < ages[j] < 100):
                    continue
                if ages[i] in neighbors.keys():
                    neighbors[ages[i]].append(ages[j])
                else:
                    neighbors[ages[i]] = [ages[j]]
        for v in neighbors.values():
            res += len(v)
        return res






n = Solution()
ages = [20,30,100,110,120]
ages = [16,17,18]
print(n.numFriendRequests(ages))