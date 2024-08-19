class Solution:
    def reverseStr(self, s: str, k: int) -> str: 
        i = 0
        while i < len(s):
            i2 = i + k
#对某一片段反转，采用列表切片嵌套“s[i:i2][::-1]”表示s截取 从索引 i 到索引 i2（不包括i2）的片段后再reverse
#列表之间可以用加号直接拼凑
            s = s[:i] + s[i:i2][::-1] + s[i2:]
            i = i + 2 * k
        return s