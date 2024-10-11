class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:

        ans = 1
        temp = 1

        for i in range(len(nums) - 1):
            if nums[i+1] > nums[i]:
                temp += 1
                ans = max(ans , temp)
            else:
                temp = 1

        return ans