from COR.Rule import Rule


class VerticalRule(Rule):

    def isRuleValid(self, row, col, board, value, knight_flag, king_flag, board_length):
        print("Going to apply vertical rule")
        for i in range(board_length):
            if board[i][col] == value:
                print("Vertical Ruled Failed")
                return False
        return super().isRuleValid(row, col, board, value, knight_flag, king_flag, board_length)
