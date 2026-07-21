class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        
        length = len(cost)
        if length == 1:
            return cost[0]
        
        costAtStep = [0] * (len(cost) + 1)

        costAtStep[0] = 0
        costAtStep[1] = 0
    
        for step in range(2,length + 1):
            costAtStep[step] = min(costAtStep[step-1] + cost[step-1],
            costAtStep[step-2] + cost[step-2])
        
        return costAtStep[-1]



#[1,2,1,2,1,1,1]
#[1,2,2,4,3,4,4]