class Solution:
 def romanToInt(self, s: str) -> int:
    d1={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    d2={'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    temp=0
    i=0
    while i < len(s):
        if s[i:i+2] in d2:
            temp += d2[s[i:i+2]]
            i += 2
        else:
            temp += d1[s[i]]
            i += 1
    return temp
case=Solution()
print(case.romanToInt('MCMXCIV'))
