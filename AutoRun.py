from COR.RuleChain import Chain
from Board import Board
import random


class AutoRun:
    board = Board()
    chain = Chain()

    def autoChecker(self, board, knight_flag, king_flag, board_length):
        for rowCheck in range(board_length):
            for columnCheck in range(board_length):
                self.board.print_board()
                if board[rowCheck][columnCheck] != 0:
                    if rowCheck == board_length and \
                            columnCheck == board_length and \
                            board[rowCheck][columnCheck] != 0:
                        print("Finished")
                        self.board.print_board()
                else:
                    lister = []
                    while True:
                        n = random.randint(1, board_length)
                        if len(lister) == board_length:
                            break
                        else:
                            if n in lister:
                                pass
                            else:
                                lister.append(n)
                                result = self.initiateRuleCheckingProcess(rowCheck, columnCheck, n, knight_flag,
                                                                          king_flag, board_length)
                                if result:
                                    self.board.updateBoard(rowCheck, columnCheck, n)
                                    break
                                else:
                                    print("next")
            self.board.print_board()
            print('\n')
        filler = self.board.isNotBoardFilled()
        if filler:
            print("Not solvable")
        else:
            print("Solvable")

    def initiateRuleCheckingProcess(self, row, column, value, knight_flag, king_flag, board_length):
        return self.chain.process(row, column, self.board.getSudokuBoard(), value, knight_flag, king_flag, board_length)
