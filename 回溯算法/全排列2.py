class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        used = [0] * len(nums)
        nums.sort()
        
        def backtracking(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                    continue
                used[i] = 1
                path.append(nums[i])
                backtracking(path)
                path.pop()
                used[i] = 0
        
        backtracking([])
        return res