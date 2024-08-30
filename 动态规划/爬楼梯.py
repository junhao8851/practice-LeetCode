class Solution:
    def climbStairs(self, n: int) -> int:
        #solutions[]是一个初值为1，1的斐波那契数列
        #递归调用会超时,于是把前n项手动append，并return第n项
        solutions = [1,2]
        if n <= 2:
            return solutions[n - 1]
        while len(solutions) < n:
            solutions.append(solutions[-1] + solutions[-2])
        return solutions[n - 1] #或者solutions[-1]