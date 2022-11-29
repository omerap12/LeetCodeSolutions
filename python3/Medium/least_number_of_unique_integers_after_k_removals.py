# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/description/
import heapq


class Solution:
    def findLeastNumOfUniqueInts(self, arr, k):
        unique_numbers = set(arr)
        dict_numbers = {}
        for number in arr:
            if number in dict_numbers.keys():
                dict_numbers[number] += 1
            else:
                dict_numbers[number] = 1
        heap_numbers = [(v, k) for k, v in dict_numbers.items()]  # (a,b): a->number of elements, b -> type of element
        heapq.heapify(heap_numbers)

        while heap_numbers:
            number_of_elements, element = heapq.heappop(heap_numbers)
            if number_of_elements <= k:
                unique_numbers.remove(element)
                k -= number_of_elements
            else:
                return len(unique_numbers)
        return len(unique_numbers)


n = Solution()
arr = [4, 3, 1, 1, 3, 3, 2]
k = 2
# arr = [5,5,4]
# k = 1
print(n.findLeastNumOfUniqueInts(arr, k))
