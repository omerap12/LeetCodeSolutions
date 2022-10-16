# https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf(self, nums):
        product = 1
        zero_index = set()
        flag = False
        for i in range(len(nums)):
            if nums[i] == 0:
                flag = True
                zero_index.add(i)
            else:
                product = product*nums[i]
        answer = []
        for i in range(len(nums)):
            if flag and i not in zero_index:
                answer.append(0)
            elif flag and i in zero_index:
                if len(zero_index) == 1:
                    answer.append(product)
                else:
                    answer.append(0)
            else:
                answer.append(int(product/nums[i]))
        return answer
