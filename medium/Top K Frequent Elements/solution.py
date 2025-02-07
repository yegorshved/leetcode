def topKFrequent(nums: list[int], k: int) -> list[int]:
  numset = set(nums)
  nummap = {i: 0 for i in numset}
  # print(nummap)
  for n in nums:
      nummap[n] += 1
  maxarr = [0] * k
  #print(nummap)

  for i in range(k):
    maxarr[i] = max(nummap, key=nummap.get)
    del nummap[maxarr[i]]
    
  return maxarr

nums=[1,1,1,1,1,1,1,12,2 ,3,3,3,3,3]
k=2
print(topKFrequent(nums, k))