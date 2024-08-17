class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 使用set集合里的方法intersection
        # 前提是交集内的元素要求不重复，若交集元素可重复（比如都有两个2，交集里也须有两个2），考虑用哈希表或双指针
        return list(set(nums1) & set(nums2))  
	
