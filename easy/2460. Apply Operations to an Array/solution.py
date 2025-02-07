from typing import List

def applyOperations(nums: List[int]) -> List[int]:
    
    # we need to apply n - 1 operations
    n = len(nums)
    
    for i in range(n - 1):
        if nums[i] == nums[i + 1]:
            nums[i]*=2
            nums[i+1]=0
    # shift all 0's to the end of the array
    # I don't want to overcomplicate this, 
    # so I simply use another array filled with zeros
    result = [0] * n
    result_iterator = 0
    for i in range(n):
      if nums[i] != 0:
        result[result_iterator] = nums[i]
        result_iterator+=1
    return result





nums1 = [847,847,0,0,0,399,416,416,879,879,206,206,206,272]
print(applyOperations(nums1))
# expected:
# [1694,399,832,1758,412,206,272,0,0,0,0,0,0,0]
