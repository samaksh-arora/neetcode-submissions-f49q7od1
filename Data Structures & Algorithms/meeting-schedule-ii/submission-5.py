"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        meetingEndTimes = []
        intervals.sort(key = lambda interval: interval.start)
        for interval in intervals:
            if meetingEndTimes and meetingEndTimes[0] <= interval.start:
                heapq.heappop(meetingEndTimes)
            heapq.heappush(meetingEndTimes, interval.end)

        return len(meetingEndTimes)