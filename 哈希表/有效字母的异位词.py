class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
# collections.Counter()返回一个字典
        counter_s = collections.Counter(s)
        counter_t = collections.Counter(t)
        return counter_s == counter_t