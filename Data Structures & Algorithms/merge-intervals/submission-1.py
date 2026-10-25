class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        if len(intervals) == 0:
            return intervals

        intervals.sort()
        result = []
        left = 0
        right = 1
        while right < len(intervals):
            currStart, currEnd = intervals[left]
            nextStart, nextEnd = intervals[right]

            if currEnd >= nextStart:
                intervals[left] = [currStart, max(currEnd, nextEnd)]
            else:
                result.append(intervals[left])
                left = right
            right += 1
        result.append(intervals[left])
    
        return result