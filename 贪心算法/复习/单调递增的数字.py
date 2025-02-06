class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = [int(i) for i in list(str(n))]
        if len(digits) == 1: return n

        for i in range(len(digits)-1, 0, -1):
            if digits[i] < digits[i - 1]:
                digits[i:] = [9] * (len(digits) - i)
                digits[i - 1] -= 1

        res = 0
        for num in digits: res = res * 10 + num
        return res

