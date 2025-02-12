class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        original = nums[0]
        index = 1
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != original:
                nums[index] = nums[i]
                original = nums[i]
                index+=1
                k+=1
        return k

