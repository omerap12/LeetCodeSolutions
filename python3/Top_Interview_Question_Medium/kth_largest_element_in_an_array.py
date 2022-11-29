# https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution(object):
    def findKthLargest(self, nums, k):
        if not nums:
            return
        random_pivot = random.choice(nums)
        left = [v for v in nums if v < random_pivot]
        right = [v for v in nums if v > random_pivot]
        mid = [v for v in nums if v == random_pivot]

        length_right = len(right)
        length_mid = len(mid)

        # if the kth largest element is within the right array
        if k <= length_right:
            return self.findKthLargest(right, k)
        # if the kth largest element is within the left array, adjust k accordingly
        if k > length_right + length_mid:
            return self.findKthLargest(left, k - length_right - length_mid)
        else:
            # the kth element is the pivot
            return mid[0]
