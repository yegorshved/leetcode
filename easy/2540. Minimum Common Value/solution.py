class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1)>len(nums2):
            return self.getCommon(nums2,nums1)
        
        hset = set(nums1)
        for i in nums2:
            if i in hset:
                return i
        return -1
