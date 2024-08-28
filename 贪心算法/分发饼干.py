class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()

        i = 0
        kid = 0 
        
        for size in s:
            #必须加这一句，否则若len(s)>len(g),g的指针i会超出范围
            if i == len(g):
                break

            if g[i] <= size:
                i += 1
                kid += 1

        return kid