Solution To: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/

class Solution(object):
    def rotate(self, nums, k):
        """
        observation: when rotating k-times array is like taking the [k'th index number of the array:end of the array 
        to be the first elements of the answer and the [0:k index numbers of the array] to be the last elements of 
        the answer array 
        :param nums: array given
        :param k: how many rotates
        :return: rotated array
        """
        answer = [0] * len(nums)
        iter_times = k % len(nums)  # to prevent all round rotating (means no need to rotate a thing) so we take the 
        # modulo 
        index_start = len(nums) - iter_times  # last index of the first k'th element
        index_start_answer = 0
        for i in range(index_start, len(nums), 1):  # copy k'th element to end
            answer[index_start_answer] = nums[i]
            index_start_answer += 1
        for i in range(index_start):  # copy first kth element
            answer[index_start_answer + i] = nums[i]
        return answer
