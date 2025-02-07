def removeDuplicates(nums: list[int]) -> int:
  orig = nums[0]
  orig_index = 1
  orig_number=1
  for i in range(1, len(nums)):
    if nums[i] == orig:
      continue
    if nums[i] != orig:
      nums[orig_index] = nums[i]
      orig_index+=1
      orig = nums[i]
      orig_number+=1
      continue
  return orig_number

    




nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))
print(nums)
