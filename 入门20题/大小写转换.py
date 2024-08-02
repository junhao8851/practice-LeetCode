class Solution:
    def toLowerCase(self, s: str) -> str:
        return str.lower(s)# str.lower()函数和str.upper()函数可直接调用

    另外可以用ASCII码转换
'A' - 'Z' 对应的 ascii 是 65 - 90；

'a' - 'z' 对应的 ascii 是 97 - 122；

大小字母转换相差32，只要记住ord(),chr()函数即可  ordinal    character
class Solution:

    def toLowerCase(self, str: str) -> str:
        s = []
        for i in str:
            if  65 <= ord(i) <= 90:
                s.append(chr(ord(i) + 32))
            else:
                s.append(i)
        return ''.join(s)

