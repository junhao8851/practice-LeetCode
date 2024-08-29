class Solution:
    def jump(self, nums: List[int]) -> int:

        #贪心思路，做到局部最优（使每一步收益最大化，注意不一定是跳最远才收益最大）
        if len(nums) = 1:
            return 0

        step = 0 # 步数
        nextDistance = 0 # 下一步覆盖最远下标
        curDistance  = 0 # 当前覆盖的最远下标

        for i in range(len(nums) - 1):
            nextDistance = max(nextDistance ,i + nums[i]) # 更新下一步覆盖最远距离下标
            if i == curDistance : # 如果当前覆盖最远距离下标不是终点
                curDistance = nextDistance # 更新当前覆盖最远距离下标（相当于加油了）
                step += 1 # 需要走下一步

        return step
