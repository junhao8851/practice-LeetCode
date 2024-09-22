class Solution:
    def merge(self, intervals):
        result = []
        if len(intervals) == 0:
            return result  

        intervals.sort(key=lambda x: x[0])  # 按照区间的左边界进行排序

        result.append(intervals[0])  # 先把第一个区间直接放入结果中

        for i in range(1, len(intervals)):
            if result[-1][1] >= intervals[i][0]:  # 有重叠区间
                # 合并区间，只需要更新结果集最后一个区间的右边界
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])  