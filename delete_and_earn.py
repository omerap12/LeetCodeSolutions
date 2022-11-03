# https://leetcode.com/problems/delete-and-earn/
class Solution:
    def deleteAndEarn(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dict_numbers = {}
        for number in nums:
            if number in dict_numbers.keys():
                dict_numbers[number] += 1
            else:
                dict_numbers[number] = 1
        nums.sort()
        dp = [0] * len(dict_numbers.keys())
        used_numbers = set()
        pointer = 0
        for number in nums:
            if number not in used_numbers:
                if number-1 not in dict_numbers.keys():
                    if pointer - 1 < 0:
                        dp[pointer] = dict_numbers[number] * number
                    elif pointer - 2 < 0:
                        dp[pointer] = dict_numbers[number] * number + dp[pointer-1]
                    else:
                        dp[pointer] = dict_numbers[number] * number+max(dp[pointer-1],dp[pointer-2])
                else:
                    dp[pointer] = max(dp[pointer - 1], dp[pointer - 2] + number*dict_numbers[number])
                used_numbers.add(number)
                pointer += 1
        return dp[-1]