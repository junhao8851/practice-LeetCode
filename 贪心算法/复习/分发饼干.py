lass Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 将胃口和饼干排序
        g.sort()
        s.sort()
        # 孩子的数量
        n = len(g)
        # 饼干的数量
        m = len(s)
        # 记录结果
        res = 0 
        for i in range(m):
            # 从胃口小的开始喂
            if res < n and g[res] <= s[i]:
                res += 1
        return res

