from COR.Rule import Rule


class KnightRule(Rule):

    def isRuleValid(self, row, col, board, value, knight_flag, king_flag, board_length):

        if knight_flag == 0:
            print("Knight rule is not applied.")
            return super().isRuleValid(row, col, board, value, knight_flag, king_flag, board_length)

        else:
            row_check = [-2, -1, -2, -1, 1, 2, 2, 1]
            column_check = [-1, -2, 1, 2, -2, -1, 1, 2]
            print("Going to apply Knight rule")

            for i in range(board_length - 1):
                x = row + row_check[i]
                y = col + column_check[i]
                if board_length - 1 >= x >= 0 and \
                        0 <= y <= board_length - 1:
                    if board[x][y] == value:
                        print("Knight Rule Failed")
                        return False
                    else:
                        pass
                else:
                    pass

            return super().isRuleValid(row, col, board, value, knight_flag, king_flag, board_length)
