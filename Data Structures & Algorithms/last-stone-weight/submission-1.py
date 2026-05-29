class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)

        while stones:
            if len(stones) == 1:
                return -stones[0]
            heaviestStone = -heapq.heappop(stones)
            secondHeaviestStone = -heapq.heappop(stones)

            remainder = heaviestStone - secondHeaviestStone
            if remainder != 0:
                heapq.heappush(stones, -remainder)
            
            if len(stones) == 1:
                return -stones[0]
            
        return 0
            



        



