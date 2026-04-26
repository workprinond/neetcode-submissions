import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.k = k
        self.max_heap = [-value for value in nums]
        heapq.heapify(self.max_heap)

    def add(self, val: int) -> int:

       
        heapq.heappush(self.max_heap, -val)

        temp =[]
        for _ in range(self.k):
            temp.append(-heapq.heappop(self.max_heap))

        for item in temp:
            heapq.heappush(self.max_heap, -item)

        return temp[-1]

        
        
