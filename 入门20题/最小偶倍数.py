class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 1:
         return 2*n
        else:
         return n

#n为奇数时return 2*n，n为偶数时return n，故可直接return （n % 2 + 1）*n