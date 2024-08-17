class Solution:
    def isHappy(self, n: int) -> bool:
        record = {1} #给集合里赋一个1，当n迭代到1时可以直接判n是否等于1，如果不赋初值1，需要迭代到第二次1才能退出循环
        while n not in record:
            record.add(n)
            n = sum(int(i) ** 2 for i in str(n))
        return n == 1