class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = []
        res = []

        #确定递归参数
        def dfs(i):

        #边界条件
            if i == n:
                res.append(path.copy()) # 因为path会变，引起res也变，故要把每种走完了的path固定append给res
                return

        #单层逻辑    
            path.append(nums[i])
            dfs(i+1)
            path.pop() #回溯
            dfs(i+1)

        #递归入口为 i=0
        dfs(0)

        return res