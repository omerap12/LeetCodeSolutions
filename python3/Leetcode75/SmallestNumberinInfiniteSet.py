import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.numbers_set = set()
        self.heap = []
        for i in range(1000):
            self.heap.append(i)
            self.numbers_set.add(i)
        heapq.heapify(self.heap)

    def popSmallest(self) -> int:
        pulled = heapq.heappop(self.heap)
        self.numbers_set.remove(pulled)
        return pulled

    def addBack(self, num: int) -> None:
        if num not in self.numbers_set:
            self.numbers_set.add(num)
            heapq.heappush(self.heap,num)