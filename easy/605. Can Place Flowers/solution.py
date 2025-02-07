def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    
    for i, k in enumerate(flowerbed):
        
        if k == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
            n-=1
            flowerbed[i] = 1
   
    return n <= 0

test_cases = [
    ([1, 0, 0, 0, 1], 1, True),
    ([1, 0, 0, 0, 1], 2, False),
    ([1, 0, 0, 0, 1], 1, True),
    ([0, 0, 1, 0, 0], 1, True),
    ([0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0], 4, True), #
    ([1, 0, 0, 0, 0, 0, 1], 2, True),
    ([0], 1, True), # 
    ([1, 0, 0, 0, 0, 1], 2, False)
]

for flowerbed, n, expected in test_cases:
    result = canPlaceFlowers(flowerbed[:], n)  # Use a copy to avoid modifying original
    #print(f"Input: {flowerbed}, {n} -> Output: {result} (Expected: {expected})")
    print(f"{result} {expected}")

#print(canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))