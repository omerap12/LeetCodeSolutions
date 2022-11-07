class Solution:
    def deleteAndEarn(self, nums):
        sum_of_odd = 0
        sum_of_even = 0
        for number in nums:
            if number % 2 == 0:
                sum_of_even += number
            else:
                sum_of_odd += number
        return max(sum_of_odd,sum_of_even)

n = Solution()
nums = [2,3,4]
print(n.deleteAndEarn(nums))
# nums = [2,2,3,3,3,4]
# print(n.deleteAndEarn(nums))