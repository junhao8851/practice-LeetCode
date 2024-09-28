class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
         ans = []
         path = []

         def dfs(i , left):
            # 边界条件
            if left == 0:
                ans.append(path.copy())
                return
            if i == len(candidates) or left < 0:
                return

            #当前逻辑（选或不选）
            path.append(candidates[i])
            dfs(i, left - candidates[i])
            path.pop()

            dfs(i + 1, left)

         dfs(0 , target)
         return ans
