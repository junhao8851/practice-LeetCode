class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        nums = [int(i) for i in str(n)] 
# 此行尤为关键，str(n)里如果不声明i是整数型变量，nums列表里的元素将会是字符串而非数字
# 这是把一个数的各位取出放入列表里的通用方法之一

        sum_ = 0
        product_= 1
# 为各位之和与乘积分别赋初值0和1

        for i in nums:
            sum_ += i
            product_ *= i
        return product_ - sum_
# 把列表里的各位数字遍历相加，相乘
