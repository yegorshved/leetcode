class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        n = rowIndex + 1
        for i in range(n):
            current_row = [1] * (i + 1)
            for j in range(1, i):
                current_row[j] = row[j-1] + row[j]
            row = current_row
        return row
