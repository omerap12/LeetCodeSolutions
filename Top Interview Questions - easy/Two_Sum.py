Solution To: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/

class Solution(object):
    def twoSum(self, nums, target):
        sorted_nums = sorted(nums)
        index_start = 0
        index_end = len(sorted_nums) - 1

        while index_start != index_end: # two pointers in sorted array , one at min value , second at max value
            if sorted_nums[index_start] + sorted_nums[index_end] == target: # if min+max == target call aux for returning matching indexes
                indexes_in_nums = [nums.index(sorted_nums[index_start]),nums.index(sorted_nums[index_end])]
                return self.find_indexes(indexes_in_nums, nums, sorted_nums)
            if sorted_nums[index_start] + sorted_nums[index_end] < target: # if min+max<target get raise min value (move pointer forward)
                index_start += 1
            if sorted_nums[index_start] + sorted_nums[index_end] > target: # if min+max>target get lower max value (move pointer backward)
                index_end -= 1

    def find_indexes(self, indexes, nums): # check if indexes not mathcing if so retun indexe
        if indexes[0] != indexes[1]:
            return indexes
        answer = [i for i, x in enumerate(nums) if x == nums[indexes[0]]] # get all indexes
        return answer
