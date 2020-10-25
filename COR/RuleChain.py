from COR.HorizontalRule import HorizontalRule
from COR.VerticalRule import VerticalRule
from COR.MiniBoardRule import MiniBoardRule
from COR.KnightRule import KnightRule
from COR.KingRule import KingRule


class Chain:
    def __init__(self):
        self.rule4 = KingRule(None)
        self.rule3 = KnightRule(self.rule4)
        self.rule2 = HorizontalRule(self.rule3)
        self.rule1 = VerticalRule(self.rule2)
        self.rule = MiniBoardRule(self.rule1)

    def process(self, row, column, board, value, knight_flag, king_flag, board_length):
        return self.rule.isRuleValid(row, column, board, value, knight_flag, king_flag, board_length)
