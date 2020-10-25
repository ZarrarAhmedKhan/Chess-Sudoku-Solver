from COR.Rule import Rule


class MiniBoardRule(Rule):
    miniBoardLength = 3

    def isRuleValid(self, row, col, board, value, knight_flag, king_flag, board_length):
        print("Going to apply mini board rule")
        boxFinderRow = int(row / self.miniBoardLength)
        boxFinderColumn = int(col / self.miniBoardLength)

        actualBoardStartRow = boxFinderRow * self.miniBoardLength
        actualBoardStartColumn = boxFinderColumn * self.miniBoardLength

        actualBoardEndRow = actualBoardStartRow + (self.miniBoardLength - 1)
        actualBoardEndColumn = actualBoardStartColumn + (self.miniBoardLength - 1)

        for i in range(actualBoardStartRow, actualBoardEndRow + 1):
            for j in range(actualBoardStartColumn, actualBoardEndColumn + 1):
                if board[i][j] == value:
                    print("MiniBoard Rule Failed")
                    return False
        return super().isRuleValid(row, col, board, value, knight_flag, king_flag, board_length)
