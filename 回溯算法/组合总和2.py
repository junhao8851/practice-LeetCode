class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #枚举法（先sort），与选或不选（题目组合总和1）区分开
        n = len(candidates)
        ans = []
        path = []
        candidates.sort()

        def dfs(i, curr):

            if curr == 0:
                ans.append(path[:])
                return

            for j in range(i, n):
                if j > i and candidates[j] == candidates[j-1]:#跳过相同元素
                    continue
                if curr < candidates[i]: #剪枝
                    break 
                path.append(candidates[j])
                dfs(j+1, curr-candidates[j])
                path.pop()

        dfs(0, target)
        return ans