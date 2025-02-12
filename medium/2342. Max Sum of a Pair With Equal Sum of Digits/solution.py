class Solution:
  def get_num_sum(self, digit: int) -> int:
    res = 0
    temp = digit
    while temp:
      res += temp % 10
      temp //= 10
    return res
  
  def maximumSum(self, nums: List[int]) -> int:
    maxsums = [-1] * 82
    result = -1
    for i, n in enumerate(nums):
      temp = self.get_num_sum(n)
      if maxsums[temp] == -1:
        maxsums[temp] = n
      else:
        result = max(result, n + maxsums[temp])
      
      maxsums[temp] = max(maxsums[temp], n)
    
    return result
