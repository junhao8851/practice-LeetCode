class Solution:
    def twoSum(self, nums, target: int) :
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
case = Solution()
print(case.twoSum([2,7,11,15],9))
