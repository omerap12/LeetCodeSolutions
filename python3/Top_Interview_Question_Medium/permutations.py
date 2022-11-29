# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums):
        """
        using backtracking
        """
        answer = []
        temp_array = []
        self.backtracking(nums,answer,temp_array)
        return answer

    def backtracking(self,nums,answer,tmp):
        if len(tmp) == len(nums):
            answer.append(tmp.copy())
        else:
            for i in range(len(nums)):
                # don't get duplicate numbers
                if nums[i] not in tmp:
                    tmp.append(nums[i])
                    self.backtracking(nums,answer,tmp)
                    # backing from the recursion, switching the numbers in the array
                    tmp.pop(len(tmp)-1)


nums = [1,2,3]
n = Solution()
print(n.permute(nums))
