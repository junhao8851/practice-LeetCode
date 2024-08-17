class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 针对较短数组进行遍历将元素存于哈希表中
        # 保证前面的数组较短
        if len(nums1) > len(nums2):
            self.intersect(nums2, nums1)
        
        hash_map = {}
        for num in nums1:
            if num not in hash_map:
                hash_map[num] = 0
            hash_map[num] += 1
        #这段把nums1写入字典hash_map中，也可以用hash_map = collections.Counter(nums1)
        
        ans = []

        for num in nums2:
            # 查看是否存在于哈希表中
            count = hash_map.get(num, 0)
            # 元素存在于哈希表中，则添加入结果列表中
            # 然后将哈希表对应的元素出现次数减一
            if count > 0:
                ans.append(num)
                hash_map[num]-=1
        
        return ans