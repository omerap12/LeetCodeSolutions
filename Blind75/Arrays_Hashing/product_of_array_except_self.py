# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums):
        prefix_product = []
        suffix_product = [0]*len(nums)
        current_product = 1
        for i in range(len(nums)):
            current_product *= nums[i]
            prefix_product.append(current_product)
        current_product = 1
        for j in range(len(nums) - 1, -1,-1):
            current_product *= nums[j]
            suffix_product[j] = current_product
        answer = [0]*len(nums)
        for i in range(len(nums)):
            if 0 < i < len(nums)-1:
                answer[i] = prefix_product[i-1]*suffix_product[i+1]
            elif i == 0:
                answer[i] = suffix_product[i+1]
            else:
                answer[i] = prefix_product[len(nums)-2]
        return answer
