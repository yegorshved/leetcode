class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
      
        hset1 = set(nums1)
        hset2 = set(nums2)
        
        for i in nums2:
            if i in hset1:
                hset1.remove(i)
                hset2.remove(i)
        
        return [list(hset1), list(hset2)]
