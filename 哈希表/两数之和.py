class Solution:
#哈希表法，对于v，查找target - v是否在键里
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = dict()

        for k,v in enumerate(nums):
            
            if target - v in records:
                return [records[target - v],k]
                
            records[v] = k