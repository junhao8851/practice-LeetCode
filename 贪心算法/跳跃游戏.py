class Solution:
    def canJump(self, nums: List[int]) -> bool:

        #关键看每个索引往前覆盖的范围边界

        edge = 0 #edge是往前覆盖的边界索引值，随着i的移动，不断尝试更新

        for i,v in enumerate(nums):
            
            if i > edge: #则无法到达索引 i 处
                return False

            edge = max(edge , i + v)
            
        return True