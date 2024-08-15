class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums[::2], nums[1::2] = nums[:n], nums[n:]
#python列表切片语法
#必须一次赋值，不能分两句
        return nums