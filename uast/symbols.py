import operator
from collections import namedtuple
from enum import Enum

Symbol = Enum('Symbol', [
    'GETATTR', 'GETITEM', 'AND', 'OR', 'NOT', 'ADD', 'SUB', 'MUL', 'DIV', 'EQ',
    'GT', 'GE', 'LT', 'LE', 'VAR',
])


Operator = namedtuple('Operator', ['symbol', 'format', 'operator', 'method'])


operators = {
    Symbol.GETATTR: Operator(
        Symbol.GETATTR, '{0!r}.{1!r}', getattr, '__getattr__'),
    Symbol.GETITEM: Operator(
        Symbol.GETITEM, '{0!r}["{1!r}"]', operator.getitem, '__getitem__'),
    Symbol.AND: Operator(Symbol.AND, '{0!r} and {1!r}', operator.and_, None),
    Symbol.OR: Operator(Symbol.OR, '{0!r} or {1!r}', operator.or_, None),
    Symbol.NOT: Operator(Symbol.NOT, 'not {0!r}', operator.not_, None),
    Symbol.ADD: Operator(Symbol.ADD, '{0!r} + {1!r}', operator.add, '__add__'),
    Symbol.SUB: Operator(Symbol.SUB, '{0!r} - {1!r}', operator.sub, '__sub__'),
    Symbol.MUL: Operator(Symbol.MUL, '{0!r} * {1!r}', operator.mul, '__mul__'),
    Symbol.DIV: Operator(
        Symbol.DIV, '{0!r} / {1!r}', operator.truediv, '__truediv__'),
    Symbol.EQ: Operator(Symbol.EQ, '{0!r} == {1!r}', operator.eq, '__eq__'),
    Symbol.GT: Operator(Symbol.GT, '{0!r} > {1!r}', operator.gt, '__gt__'),
    Symbol.GE: Operator(Symbol.GE, '{0!r} >= {1!r}', operator.ge, '__ge__'),
    Symbol.LT: Operator(Symbol.LT, '{0!r} < {1!r}', operator.lt, '__lt__'),
    Symbol.LE: Operator(Symbol.LE, '{0!r} <= {1!r}', operator.le, '__le__'),
    Symbol.VAR: Operator(Symbol.VAR, '{0!r}', None, None),
}
