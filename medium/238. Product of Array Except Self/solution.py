class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        prefix = [0] * n
        prefix[0] = 1 
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        suffix = [0] * n
        suffix[n - 1] = 1

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        result = []

        for i in range(n):
            result.append(suffix[i] * prefix[i])
        
        return result
