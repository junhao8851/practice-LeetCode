class Solution:
    def addDigits(self, num: int) -> int:
        if num % 9 == 0 and num != 0:
            return 9
        else:
         return(num % 9)
# 各位之和为个位数时return此个位数，可以证明当num可以整除9时，结果一定是9；否则一定是余数（算法的魅力）
# 或者把各数位上的数拆出来相加，暴力判断