class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if not fruits:
            return 0
        
        leftPtr = 0

        typesOfFruit = {}

        count = 0

        for rightPtr in range(len(fruits)):
            typesOfFruit[fruits[rightPtr]] = typesOfFruit.get(fruits[rightPtr],0) + 1
            
            while len(typesOfFruit) > 2:
                typesOfFruit[fruits[leftPtr]] -= 1
                if typesOfFruit[fruits[leftPtr]] == 0:
                    del typesOfFruit[fruits[leftPtr]]
                leftPtr += 1
            
            count = max(count, rightPtr - leftPtr + 1)
        
        return count
