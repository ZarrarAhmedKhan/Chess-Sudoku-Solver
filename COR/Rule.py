from abc import ABC, abstractmethod


class Rule(ABC):
    def __init__(self, rule):
        self.__nextRule = rule
        super().__init__()

    @abstractmethod
    def isRuleValid(self, row, col, board, value, knight_flag, king_flag, board_length):
        if self.__nextRule is not None:
            return self.__nextRule.isRuleValid(row, col, board, value, knight_flag, king_flag, board_length)
        return True
