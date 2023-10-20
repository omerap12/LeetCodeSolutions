# https://leetcode.com/problems/summary-ranges/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        ret = []
        start = nums[0]
        curr = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == curr + 1:
                curr += 1
            else:
                if curr == start:
                    ret.append(str(start))
                else:
                    ret.append(f"{start}->{curr}")
                start = nums[i]
                curr = start
        if start == curr:
            ret.append(str(start))
            return ret
        ret.append(f"{start}->{curr}")
        return ret
            





nums = [0,1,2,4,5,7]
nums = [0,2,3,4,6,8,9]
n = Solution()
print(n.summaryRanges(nums))





nums = [0,1,2,4,5,7]
nums = [0,2,3,4,6,8,9]
n = Solution()
print(n.summaryRanges(nums))