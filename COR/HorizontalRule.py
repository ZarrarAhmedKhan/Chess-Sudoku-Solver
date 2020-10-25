from COR.Rule import Rule


class HorizontalRule(Rule):

    def isRuleValid(self, row, col, board, value, knight_flag, king_flag, board_length):
        print("Going to apply horizontal rule")
        for i in range(board_length):
            if board[row][i] == value:
                print("horizontal rule failed")
                return False
        return super().isRuleValid(row, col, board, value, knight_flag, king_flag, board_length)
