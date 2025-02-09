class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows  = {}
        cols = {}
        for i, n in enumerate(matrix):
            for j, m in enumerate(n):
                if m == 0:
                    rows[i] = 0
                    cols[j] = 0
                if i in rows or j in cols:
                    matrix[i][j] = 0

        for i, n in enumerate(matrix):
            for j, m in enumerate(n):                
                if i in rows or j in cols:
                    matrix[i][j] = 0
