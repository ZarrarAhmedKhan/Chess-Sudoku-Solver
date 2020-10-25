from Board import Board
from COR.RuleChain import Chain
from AutoRun import AutoRun


class ProcessSudoku:
    board = Board()
    chain = Chain()
    autoRun = AutoRun()

    def process(self):
        knight_flag = int(input("Do you want to apply knights constraint (1 or 0): "))
        king_flag = int(input("Do you want to apply Kings constraints (1 or 0): "))
        while self.board.isNotBoardFilled():
            checker = int(input("autorun and Check it is solvable or not. Enter '1' "))
            if checker == 1:
                if knight_flag == 1 or knight_flag == 0 or king_flag == 1 or king_flag == 0:
                    self.autoRun.autoChecker(self.board.getSudokuBoard(), knight_flag, king_flag,
                                             self.board.getBoardLength())
                    break
            else:
                row = int(input("Enter the row: "))
                column = int(input("Enter the column: "))
                value = int(input(f"Enter the value (1 - {self.board.getBoardLength()}) : "))
                if 1 <= value <= self.board.getBoardLength():
                    if knight_flag == 1 or knight_flag == 0 or king_flag == 1 or king_flag == 0:
                        self.initiateRuleCheckingProcess(row, column, value, knight_flag, king_flag)
                        print(f'knight_flag: {knight_flag}')
                        print(f'King_flag: {king_flag}')
                    else:
                        print("you entered invalid knight flag or king flag")
                        break
                else:
                    print("Value must be between 1 - 9 .")
            self.board.print_board()

    def initiateRuleCheckingProcess(self, row, column, value, knight_flag, king_flag):
        rule_chain_result = self.chain.process(row, column, self.board.getSudokuBoard(), value, knight_flag, king_flag,
                                               self.board.getBoardLength())
        if rule_chain_result:
            print("General Rule is passed, you digit is placed")
            self.board.updateBoard(row, column, value)
        else:
            print("General Rule is failed, please try again")
