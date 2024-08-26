class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        def dfs(i): 

            if i < k - len(path):
                return   #剪枝操作，剩余的个数少于还需要选的个数，则一定选不满了，这个支路就尽早切断

            if len(path) == k:
                ans.append(path.copy())
                return

            for j in range(i,0,-1): #i倒序枚举，方便剪枝
                path.append(j)
                dfs(j-1)
                path.pop()
        dfs(n)
        return ans