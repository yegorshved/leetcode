class Solution:

    def checkArray(self, row: List[str]) -> bool:
        arr = [int(i) for i in row if i != '.']
        return len(arr) == len(set(arr))

    def transposeMatrix(self, board: List[List[str]]) -> List[List[str]]:
        newboard = []
        for i in range(len(board[0])):
            newrow = []
            for j in range(len(board)):
                newrow.append(board[j][i])
            newboard.append(newrow)
        return newboard

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check every row 
        for i in board:
            if not self.checkArray(i):
                return False
        #print('row')
        transposedBoard = self.transposeMatrix(board)
        # check every col
        for i in transposedBoard:
            if not self.checkArray(i):
                return False
        #print('col')
            
        # check every square
        square = 0
        while square < 9:
            arr = []
            addToI = 0
            if 3 <= square <= 5:
                addToI = 3
            elif 6 <= square <= 8:
                addToI = 6 
            for i in range(3):
                for j in range(3):
                    arr.append(board[i+addToI][j+3*(square%3)])
            if not self.checkArray(arr):
                return False
            square+=1
        
       # print('square')
        
        return True
