class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = [0]*n #必须给定长度n，否则出bug，为什么？
        ans = []

        def dfs(i,s): # i 表示当前索引， s 表示剩余可选数字集合
 
            if i == n:
                ans.append(path.copy())
                return

            for j in s:
                path[i] = j
                dfs(i + 1,s - {j} )

        dfs(0,set(nums)) #递归入口 i = 0 ，初始可选集合即nums
        return ans