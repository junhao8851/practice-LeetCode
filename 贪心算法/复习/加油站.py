class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(cost)):
            rest = gas[i] - cost[i]  # 记录剩余油量
            index = (i + 1) % len(cost)  # 下一个加油站的索引

            while rest > 0 and index != i:  # 模拟以i为起点行驶一圈（如果有rest==0，那么答案就不唯一了）
                rest += gas[index] - cost[index]  # 更新剩余油量
                index = (index + 1) % len(cost)  # 更新下一个加油站的索引

            if rest >= 0 and index == i:  # 如果以i为起点跑一圈，剩余油量>=0，并且回到起始位置
                return i  # 返回起始位置i

        return -1  # 所有起始位置都无法环绕一圈，返回-1