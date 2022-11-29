# https://leetcode.com/problems/permutations-ii/

class Solution(object):
    def permuteUnique(self, nums):
        answer = []
        tmp = []
        answer_set = set()
        self.backtracking(nums,answer,tmp,answer_set)
        return answer
    
    def backtracking(self,nums,answer,tmp,answer_set):
        if len(nums) == len(tmp):
            if tuple(tmp) not in answer_set:
                answer.append(tmp.copy())
                answer_set.add(tuple(tmp))
        else:
            for i in range(len(nums)):
                if tmp.count(nums[i])+1 <= nums.count(nums[i]):
                    tmp.append(nums[i])
                    self.backtracking(nums,answer,tmp,answer_set)
                    tmp.pop(len(tmp)-1)