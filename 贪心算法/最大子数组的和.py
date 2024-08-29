class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        #res初值设为负无穷，防止nums全为负的情况
        res = -float('inf')
        count = 0

        for i in range(len(nums)):
             count += nums[i]

             if count > res:
                #res负责更新最大子数组之和
                res = count

             #当count加成一个非正数时，归零，从零开始重新加
             if count <= 0:
                count = 0

        return res