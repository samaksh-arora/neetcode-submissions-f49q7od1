"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        if len(intervals) == 1:
            return 1

        sortedIntervals = sorted(intervals, key = lambda interval: interval.start)
        
        activeIntervalEndTimes = []
        #^ this heap will take show the next ending meeting
        #Now we loop through a sorted version of our intervals
        #And compare every single meeting start time to the next one ending
        # and ofc if next meeting ending is before this one starts then we dont need another room

        for currentMeeting in sortedIntervals:
            if activeIntervalEndTimes and activeIntervalEndTimes[0] <= currentMeeting.start:
                heapq.heappop(activeIntervalEndTimes)

            heapq.heappush(activeIntervalEndTimes, currentMeeting.end)
        
        return len(activeIntervalEndTimes)