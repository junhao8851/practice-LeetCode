class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        #把两个s拼接后若中间再出现至少一次s，则s是重复循环的字符串

        #要在connect_s的中间查找，防止直接查找出第一个或第二个s本身，故两个s要掐头去尾

        connect_s = s[1:] + s[:-1]

        return connect_s.find(s) != -1