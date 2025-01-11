class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])      # 根据区间终点进行升序排序
        erase = 0                               # 移除次数
        end = float("-inf")                     # 当前不重叠区间的最右侧区间的end
        for s, e in intervals: 
            if s < end:
                # 当前区间和之前的区间重叠了，把当前的区间移除，因为当前区间更靠后
                erase += 1
            else:
                # 当前区间和之前的区间不重叠，后出现的区间一定更靠右，更新end
                end = e
        return erase
