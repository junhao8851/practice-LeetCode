class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
result=Solution()
print(result.isPalindrome(8998))
