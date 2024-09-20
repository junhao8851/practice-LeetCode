class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        end, cnt = float('-inf'), 0

        #对每个区间的末尾升序排
        #s,e是每个区间的起始和末尾
        for s, e in sorted(intervals, key=lambda x: x[1]):
            if s >= end:
                end = e
            else: 
                cnt += 1

        return cnt