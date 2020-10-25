class Board:
    __sudokuBoard = []
    rows = 9
    columns = 9
    __actualBoardLength = 9

    def __init__(self):
        self.initializeBoard()

    def initializeBoard(self):
        for i in range(self.columns):
            col = []
            for j in range(self.rows):
                col.append(0)
            self.__sudokuBoard.append(col)

    def print_board(self):
        for i in range(self.__actualBoardLength):
            for j in range(len(self.__sudokuBoard[0])):
                print(f"{self.__sudokuBoard[i][j]}" + " | ", end='')
            print("")

    def updateBoard(self, r, c, v):
        self.__sudokuBoard[r][c] = v

    def getSudokuBoard(self):
        return self.__sudokuBoard

    def isNotBoardFilled(self):
        for i in range(len(self.__sudokuBoard)):
            for j in range(len(self.__sudokuBoard[0])):
                if self.__sudokuBoard[i][j] == 0:
                    return True
        return False

    def getBoardLength(self):
        return self.__actualBoardLength
