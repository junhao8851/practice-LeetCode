class Solution:
    def zero_one_knapsack(self, capacity:int,wight:List[int],value:List[int]) -> [int]:

        n = len(wight)

        def dfs(i , c):

            if i < 0:
                return 0

            if wight[i] > c:
                return dfs(i - 1,c)

            return max(dfs(i - 1 , c) , dfs(i - 1 , c - wight[i]) + value[i])

        return dfs(n - 1,capacity)