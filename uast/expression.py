# pylint: disable=E1101
from uast.symbols import Symbol as S, operator_map
from typing import Any


class Expr:
    __slots__ = ('symbol', 'args')

    def __init__(self, symbol, *args):  # type: (S, *Any) -> None
        self.symbol = symbol
        self.args = args

    def __repr__(self):
        operator = operator_map[self.symbol]
        if operator.format:
            return '{}'.format(operator.format.format(*self.args))
        return super(Expr, self).__repr__()
