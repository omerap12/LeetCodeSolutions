solution To: https://leetcode.com/problems/shuffle-the-array/


class Solution(object):
    def shuffle(self, nums, n):
        nums1 = nums[0:n]
        nums2 = nums[n:(2*n)]
        nums3 = []
        for i in range(len(nums1)):
            nums3.append(nums1[i])
            nums3.append(nums2[i])
        return nums3
