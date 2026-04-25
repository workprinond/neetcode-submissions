import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Max heap using negatives (since Python heapq is min-heap)
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)  # O(n)
        
        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)  # O(log n)
            x = -heapq.heappop(max_heap)  # O(log n)
            
            if x != y:
                heapq.heappush(max_heap, -(y - x))  # O(log n)
        
        return -max_heap[0] if max_heap else 0