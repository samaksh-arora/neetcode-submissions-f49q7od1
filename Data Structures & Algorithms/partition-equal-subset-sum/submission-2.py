class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum %2 != 0:
            return False
        
        targetSum = totalSum // 2 #All we need to check is if a subset's sum equals this number

        dp = [[False]* (targetSum+1) for _ in range (len(nums)+1)]
        
        dp[0][0] = True

        #Each dp[i][j] represents can number j be made from first i numbers in list
        # currentNumber = numbers[i-1] because each time i increases it lets one more in:
            #so when i is 0 , no numbers let in. when i is 1, i-1 = 0 numbers[0] is let  in
        for i in range(1,len(dp)):
            currentNumber = nums[i-1]
            for j in range(len(dp[0])):
                if currentNumber <= j: #include
                    dp[i][j] = dp[i-1][j-currentNumber] or dp[i-1][j]
                else:                   #exclude
                    dp[i][j] = dp[i-1][j]
        
        return dp[len(nums)][targetSum]

        

