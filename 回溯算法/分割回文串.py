class Solution:
    def partition(self, s: str) -> List[List[str]]:

        n = len(s)
        ans = []
        path = []

        def dfs(i):
            if i == n:
                ans.append(path.copy())  # 当前的path给ans
                return
            for j in range(i, n):  # 枚举子串的结束位置
                t = s[i: j + 1]
                if t == t[::-1]:  # 判断回文
                    path.append(t)
                    dfs(j + 1)
                    path.pop()  # 回溯

        dfs(0)
        return ans