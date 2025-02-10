class Solution:
    def generate(self, n: int) -> List[List[int]]:
        pascal = []
        for i in range(n):
            pascal.append([1] * (i + 1))
            for j in range(1, i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

        return pascal
