class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) < len(nums1):
            return self.intersect(nums2, nums1)
        counter = Counter(nums1)
        result = []
        for i in nums2:
            if counter[i] > 0:
                result.append(i)
                counter[i]-=1
        return result
