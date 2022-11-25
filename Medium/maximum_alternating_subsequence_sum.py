class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        """
        We can make a reduction from best-time-to-buy-and-sell-stock-ii.
        It's the same problem!!! just reversed the list :)
        """
        nums.append(0)
        nums.reverse()

        res = 0
        max_profit = 0
        current_number = nums[0]
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                max_profit = max(max_profit, nums[i + 1] - current_number)
            else:
                res += max_profit
                max_profit = 0
                current_number = nums[i+1]
        res += max_profit
        return res


n = Solution()
nums = [6, 2, 1, 2, 4, 5]
print(n.maxAlternatingSum(nums))
