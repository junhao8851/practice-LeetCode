class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i:int):

            #dfs(i)=dfs(i−1)+dfs(i−2)这是爬楼梯
            #本题的本质就是爬楼梯，每一次可以往上爬nums里任意一个数

            #边界条件
            if i == 0:
                return 1

            sum = 0
            for j in nums:
                if j <= i:
                    sum += dfs(i - j) 
            return sum #也可以直接return sum(dfs(i - j) for j in nums if x <= i)

        return dfs(target)