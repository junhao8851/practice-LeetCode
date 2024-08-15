class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = 0 
        r = n - 1
        res = [None]*n
        i = n - 1
#似乎是“三指针”，两个指针在原数组两端相向移动，第三个在新数组尾端开始移动
        while  l <= r :  # 不能是<
         if nums[r] ** 2 > nums[l] ** 2:
            res[i] = nums[r] **2
            r -= 1
         else:
            res[i] = nums[l] **2
            l += 1
         i -= 1
        return res