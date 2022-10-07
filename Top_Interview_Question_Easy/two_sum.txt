class Solution(object):
    def twoSum(self, nums, target):
        sorted_nums = sorted(nums)
        start_index = 0
        stop_index = len(nums) - 1
        lower_number = None
        higher_number = None

        while start_index < stop_index:
            if sorted_nums[start_index] + sorted_nums[stop_index] == target:
                lower_number = sorted_nums[start_index]
                higher_number = sorted_nums[stop_index]
                break
            elif sorted_nums[start_index] + sorted_nums[stop_index] < target:
                start_index += 1
            else:
                stop_index -= 1
        # find the index of the two numbers
        lower_index_found = False
        higher_index_found = False
        lower_index = None
        higher_index = None
        for i in range(len(nums)):
            if lower_index_found and higher_index_found:
                return [lower_index, higher_index]
            if not lower_index_found:
                if nums[i] == lower_number:
                    lower_index = i
                    lower_index_found = True
                    continue
            if not higher_index_found:
                if nums[i] == higher_number:
                    higher_index = i
                    higher_index_found = True
        return [lower_index, higher_index]


n = Solution()
nums = [2, 7, 11, 15]
target = 9
print(n.twoSum(nums, target))

nums = [3,2,4]
target = 6
print(n.twoSum(nums, target))

nums = [3,3]
target = 6
print(n.twoSum(nums, target))