# ACCEPTED
def twoSum(nums: list[int], target: int) -> list[int]:
  map1 = { nums[i]: i for i in range(len(nums))}

  for i in range(len(nums)):
    diff = target - nums[i]
    if diff in map1 and i != map1[diff]:
      return [i, map1[diff]]


nums=[1,3,4,2]
target=6
print(twoSum(nums, target))

