class Solution
    def numIdenticalPairs(self, nums List[int]) - int
        ans = 0
        count = collections.Counter(nums)  #collections.Counter 返回一个字典，键和值分别为元素及其出现的次数

        for k, v in count.items()
            if v  1
                ans += (v  (v - 1))  2 # 排列组合

        return ans
