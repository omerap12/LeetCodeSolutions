# https://leetcode.com/problems/make-sum-divisible-by-p/description/

class Solution:
    """
    Get the value needed to pull out from the array by using %.
    Find the subarray with the value needed to pull out.
    """
    def minSubarray(self, nums, p):
        sum_nums = sum(nums)
        if sum_nums % p == 0:
            return 0
        normalized_nums = [num % p for num in nums]
        diff = sum_nums % p

        # now find the min subarray in normalized_nums with the sum of diff
        reverse_hash_map = {0: -1}
        tmp = 0
        min_val = len(nums)
        for i in range(len(nums)):
            tmp += normalized_nums[i]
            reverse_hash_map[tmp % p] = i
            if (tmp - diff) % p in reverse_hash_map.keys():
                min_val = min(min_val, i - reverse_hash_map[(tmp - diff) % p])
        return min_val if min_val < len(nums) else -1
