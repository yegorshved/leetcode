class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        
        counter = Counter(nums[0])
        nums.remove(nums[0])
        
        for arr in nums:
            counter &= Counter(arr) 
        res = []
        for i in counter:
            res.append(i)

        return sorted(res)
