class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        sum_of_0_to_n = (n*(1+n))//2
        return sum_of_0_to_n - sum(nums)