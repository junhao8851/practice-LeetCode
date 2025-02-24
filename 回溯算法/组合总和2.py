class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        candidates.sort()

        # 从pos下标开始选择，凑成总和target的所有方案
        def backtrack(pos, target):
            if target == 0:  # 复制出一份新的
                ans.append(list(path))
…                backtrack(i + 1, target - candidates[i])
                path.pop()  # 恢复现场
        
        backtrack(0, target)
        return ans

