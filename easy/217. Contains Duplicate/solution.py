# ACCEPTED
def hasDuplicate(nums: list[int]) -> bool:
  nums.sort()
  numset = set(nums)
  numset = sorted(list(numset))
  return not numset == nums


ex1 = [1, 2, 3, 3] # true
ex2 = [1, 2, 3, 4] # false
print(hasDuplicate(ex1))
print(hasDuplicate(ex2))