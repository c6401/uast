import operator
from collections import namedtuple
from enum import Enum


Symbol = Enum('S', [
    'GETATTR', 'GETITEM', 'AND', 'OR', 'NOT', 'ADD', 'SUB', 'MUL', 'DIV', 'EQ',
    'GT', 'GE', 'LT', 'LE', 'VAR',
])


Operator = namedtuple('symbol', ['symbol', 'format', 'operator', 'method'])


operators = {
    Symbol.GETATTR: Operator(
        Symbol.GETATTR, '{0}.{1}', getattr, '__getattr__'),
    Symbol.GETITEM: Operator(
        Symbol.GETITEM, '{0}["{1}"]', operator.getitem, '__getitem__'),
    Symbol.AND: Operator(Symbol.AND, '{0} and {1}', operator.and_, None),
    Symbol.OR: Operator(Symbol.OR, '{0} or {1}', operator.or_, None),
    Symbol.NOT: Operator(Symbol.NOT, 'not {0}', operator.not_, None),
    Symbol.ADD: Operator(Symbol.ADD, '{0} + {1}', operator.add, '__add__'),
    Symbol.SUB: Operator(Symbol.SUB, '{0} - {1}', operator.sub, '__sub__'),
    Symbol.MUL: Operator(Symbol.MUL, '{0} * {1}', operator.mul, '__mul__'),
    Symbol.DIV: Operator(
        Symbol.DIV, '{0} / {1}', operator.truediv, '__truediv__'),
    Symbol.EQ: Operator(Symbol.EQ, '{0} == {1}', operator.eq, '__eq__'),
    Symbol.GT: Operator(Symbol.GT, '{0} > {1}', operator.gt, '__gt__'),
    Symbol.GE: Operator(Symbol.GE, '{0} >= {1}', operator.ge, '__ge__'),
    Symbol.LT: Operator(Symbol.LT, '{0} < {1}', operator.lt, '__lt__'),
    Symbol.LE: Operator(Symbol.LE, '{0} <= {1}', operator.le, '__le__'),
    Symbol.VAR: Operator(Symbol.VAR, '{0}', None, None),
}
