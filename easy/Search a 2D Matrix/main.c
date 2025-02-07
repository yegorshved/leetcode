int binsearch(int* arr, int size, int target){
    int l = 0;
    int r = size - 1;
    int mid;
    while (l <= r){
        mid = (l+r)/2;
        if (arr[mid] == target)
            return mid;
        else if (target > arr[mid])
            l = mid + 1;
        else 
            r = mid - 1;
    }
    return -1;
}

bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target) {
    int rows = matrixSize;
    int cols = *matrixColSize;

    int topRow = 0, botRow = rows - 1, midRow;
    while (topRow <= botRow){
        midRow = (topRow + botRow) / 2;
        if (target > matrix[midRow][cols - 1])
            topRow = midRow + 1;
        else if (target < matrix[midRow][0])
            botRow = midRow - 1;
        else
            return (-1 != binsearch(matrix[midRow], cols, target));
    }
    return 0;
}
