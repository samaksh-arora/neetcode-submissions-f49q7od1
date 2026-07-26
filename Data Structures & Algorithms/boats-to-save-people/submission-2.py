class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        leftPtr = 0
        rightPtr = len(people) -1

        #[1,2,4,5]
        count = 0
        
        while leftPtr <= rightPtr:
            sumOfWeights = people[leftPtr] + people[rightPtr]
    
            if sumOfWeights > limit: #heavier weight takes a boat
                count +=1
                rightPtr -=1
            if sumOfWeights <= limit: #add up and take the boat
                count += 1
                leftPtr += 1
                rightPtr -= 1
        
        return count
            
                

