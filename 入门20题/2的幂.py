class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(32):
            if 2 ** i == n:
                return True
        return False
# 一旦return true，函数立即停止执行，所以不会再return false
# 如果遍历指数0~31全部不等，才会return false，逻辑正确