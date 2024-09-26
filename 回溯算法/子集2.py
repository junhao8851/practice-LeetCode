class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        n = len(nums)
        nums.sort()

        def dfs(idx, tmp):
            res.append(tmp)

            for i in range(idx, n):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                dfs(i+1, tmp + [nums[i]])
                
        dfs(0, [])
        return res