# https://leetcode.com/problems/partition-equal-subset-sum/description/

class Solution:
    def canPartition(self, nums):
        sum_of_arr = sum(nums)
        if sum_of_arr % 2 != 0:
            return False
        bag_capcaity = sum_of_arr//2
        vector = [0]*len(nums)
        dp_matrix = []
        for row in range((bag_capcaity)+1):
            dp_matrix.append(vector.copy())

        for capacity in range(1,bag_capcaity+1,1):
            for index in range(1,len(nums),1):
                if capacity < nums[index]:
                    dp_matrix[capacity][index] = dp_matrix[capacity][index-1]
                else:
                    dp_matrix[capacity][index] = max(dp_matrix[capacity][index-1],dp_matrix[capacity-nums[index]][index-1]+nums[index])
        return dp_matrix[-1][-1] == sum_of_arr//2





arr = [14,9,8,4,3,2]
n = Solution()
print(n.canPartition(arr))
