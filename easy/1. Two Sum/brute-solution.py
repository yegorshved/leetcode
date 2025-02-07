#class Solution:
def twoSum(nums: list[int], target: int) -> list[int]:
  
  for i in range(len(nums) - 1):
    for j in range(1, len(nums)):
      if nums[i] + nums[j] == target:
        return [i, j]
          
print(twoSum([3, 4, 5, 6, 7], 7))
print(twoSum([4, 5, 6], 10))
print(twoSum([5, 5], 10))
print(twoSum([5, 5], 10))





    
