class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        res, trend = 1, 0

        for i in range(1, len(nums)):

            if nums[i] > nums[i-1] and trend <= 0:

                res += 1

                trend = 1

            elif nums[i] < nums[i-1] and trend >= 0:

                res += 1

                trend = -1

        return res