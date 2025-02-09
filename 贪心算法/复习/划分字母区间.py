class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        times = Counter(s)
        res = []

        stack = set()
        count = 0
        
        for e in s:
            times[e] -= 1
        return res
