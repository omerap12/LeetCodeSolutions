# https://leetcode.com/problems/intersection-of-two-arrays-ii/
class Solution(object):
    def intersect(self, nums1, nums2):
        num1_dict = {}
        num2_dict = {}
        answer = []
        for number in nums1:
            if number in num1_dict.keys():
                num1_dict[number] += 1
            else:
                num1_dict[number] = 1
        for number in nums2:
            if number in num2_dict.keys():
                num2_dict[number] += 1
            else:
                num2_dict[number] = 1
        for i in num1_dict.keys():
            if i in num2_dict.keys():
                for time in range(min(num1_dict[i],num2_dict[i])):
                    answer.append(i)
        return answer