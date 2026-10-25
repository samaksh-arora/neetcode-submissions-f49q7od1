class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #O(n)
        # O(n) space 
        if not intervals:
            return [newInterval]
        oldLength = len(intervals)
        for i in range(oldLength -1):
            interval = intervals[i]
            nextInterval = intervals[i+1]
            if newInterval[0] >= interval[0] and newInterval[0] <= nextInterval[0]:
                intervals.insert(i+1,newInterval)
        
        if oldLength == len(intervals):
            if newInterval[0] < intervals[0][0]:
                intervals.insert(0,newInterval)
            elif newInterval[0] >= intervals[-1][0]:
                intervals.append(newInterval)
        
        left = 0
        right = 1

        result = []
        while right < len(intervals):
            currentStart,currentEnd = intervals[left]
            nextStart, nextEnd = intervals[right]

            if currentEnd >= nextStart:
                intervals[left] = [currentStart, max(currentEnd, nextEnd)]
            else:
                result.append(intervals[left])
                left = right
            right += 1
        
        result.append(intervals[left])

        return result

