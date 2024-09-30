class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i):
            d = n - sum(path)   # 差值
            if d < 0:
                return 
            if len(path) == k and d == 0:
                ans.append(path.copy())
                return
                
            for j in range(i,10):
                path.append(j)
                dfs(j+1)
                path.pop()
        
        dfs(1)
        return ans