# https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/
class Solution:
    def sumEvenAfterQueries(self, nums,queries):
        """
        Find sum for all even numbers
        check for each index of queries[i], A[index] is even or not
        if A[index] is even subtract from sum
        add queries[i]'s value to A[index]
        check if A[index] is even add to sum again
        """
        sum_til_now = [0]
        res = []
        for number in nums:
            if number % 2 == 0:
                sum_til_now[0] += number
        for q in queries:
            old_val = nums[q[1]]
            nums[q[1]] += q[0]
            if nums[q[1]] % 2 != 0:
                if old_val % 2 == 0:
                    sum_til_now[0] -= old_val
            else:
                # even
                if old_val % 2 != 0:
                    sum_til_now[0] += nums[q[1]]
                else:
                    if nums[q[1]] < 0:
                        sum_til_now[0] -= old_val
                        sum_til_now[0] += nums[q[1]]
                    else:
                        sum_til_now[0] += q[0]
            res.append(sum_til_now[0])
        return res
