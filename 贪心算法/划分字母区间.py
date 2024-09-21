class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_appear= {}  # 字典存储每个字符最后出现的位置
        for i, ch in enumerate(s):
            last_appear[ch] = i

        result = []
        start = 0
        end = 0
        for i, ch in enumerate(s):
            end = max(end, last_appear[ch])  # 找到当前字符出现的最远位置
            if i == end:  # 如果当前位置是最远位置，则可以分割出一个区间
                result.append(end - start + 1) # 把区间长度存入result
                start = i + 1

        return result