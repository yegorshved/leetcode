def binsearch(mat: List[int], target) -> bool:
    l = 0
    r = len(mat) - 1
    while l <= r:
        mid = (l + r) // 2
        if mat[mid] == target:
            return True
        elif mat[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows - 1
        while left <= right:
            mid = (left + right) // 2
            if (target > matrix[mid][-1]):
                left = mid + 1
            elif (target < matrix[mid][0]):
                right = mid - 1
            else:
                return binsearch(matrix[mid], target)
        return False
