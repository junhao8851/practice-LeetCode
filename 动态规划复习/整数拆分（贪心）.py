class Solution:
    def integerBreak(self, n):
        # 本题可以用贪心，每次拆成n个3，如果剩下是4，则保留4，然后相乘，但是这个结论需要数学证明其合理性
        if n == 2:  # 当n等于2时，只有一种拆分方式：1+1=2，乘积为1
            return 1
        if n == 3:  # 当n等于3时，只有一种拆分方式：2+1=3，乘积为2
            return 2
        if n == 4:  # 当n等于4时，有两种拆分方式：2+2=4和1+1+1+1=4，乘积都为4
            return 4
        result = 1
        while n > 4:
            result *= 3  # 每次乘以3，因为3的乘积比其他数字更大
            n -= 3  # 每次减去3
        result *= n  # 将剩余的n乘以最后的结果
        return result