class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#滑动窗口，实质也是双指针
#关键在判断起始点和终止点分别何时移动
        sum = 0
        min_len = float('inf')#先给最小值赋初值正无穷，后面每次进入循环都取最小值
        left = 0
        right = 0
        while right < len(nums):
            sum += nums[right]
            while sum >= target:
              min_len = min(min_len , right - left + 1)
              sum -= nums[left]
              left += 1
            right += 1
        if min_len != float('inf'):
         return min_len
        else:
         return 0