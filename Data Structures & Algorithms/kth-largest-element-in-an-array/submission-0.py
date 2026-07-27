class Solution:
    import heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        minHeap = []

        for num in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, num)
            else:
                if minHeap[0] < num:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, num)
        
        return minHeap[0]
            
