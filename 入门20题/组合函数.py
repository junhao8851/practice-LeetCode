class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
         count = 0
         for i, j, k in itertools.combinations(arr, 3):     
    #itertools.combinations组合函数，返回若干元组，每个元组中的元素默认从小到大排序
            if abs(i - j) <= a and abs(j - k) <= b and abs(i - k) <= c:
             count += 1
         return count