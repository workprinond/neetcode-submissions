
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        
        # Sort by start attribute, not by index
        intervals.sort(key=lambda x: x.start)
        
        for i in range(len(intervals) - 1):
            # Compare end of current with start of next
            if intervals[i].end > intervals[i+1].start:
                return False
        return True