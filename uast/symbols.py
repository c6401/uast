import operator
from collections import namedtuple
from enum import Enum

Symbol = Enum('Symbol', [
    'GETATTR', 'GETITEM', 'AND', 'OR', 'NOT', 'ADD', 'SUB', 'MUL', 'DIV', 'EQ',
    'GT', 'GE', 'LT', 'LE', 'CONTAINS', 'CALL', 'VAR',
])


Operator = namedtuple('Operator', ['symbol', 'format', 'operator', 'method'])


operators = [
    Operator(Symbol.GETATTR, '{0!r}.{1}', getattr, '__getattr__'),
    Operator(Symbol.GETITEM, '{0!r}[{1!r}]', operator.getitem, '__getitem__'),
    Operator(Symbol.AND, '({0!r} and {1!r})', operator.and_, None),
    Operator(Symbol.OR, '({0!r} or {1!r})', operator.or_, None),
    Operator(Symbol.NOT, 'not {0!r}', operator.not_, None),
    Operator(Symbol.ADD, '({0!r} + {1!r})', operator.add, '__add__'),
    Operator(Symbol.SUB, '({0!r} - {1!r})', operator.sub, '__sub__'),
    Operator(Symbol.MUL, '({0!r} * {1!r})', operator.mul, '__mul__'),
    Operator(Symbol.DIV, '({0!r} / {1!r})', operator.truediv, '__truediv__'),
    Operator(Symbol.EQ, '({0!r} == {1!r})', operator.eq, '__eq__'),
    Operator(Symbol.GT, '({0!r} > {1!r})', operator.gt, '__gt__'),
    Operator(Symbol.GE, '({0!r} >= {1!r})', operator.ge, '__ge__'),
    Operator(Symbol.LT, '({0!r} < {1!r})', operator.lt, '__lt__'),
    Operator(Symbol.LE, '({0!r} <= {1!r})', operator.le, '__le__'),
    Operator(Symbol.VAR, '{0}', None, None),
    Operator(
        Symbol.CONTAINS, '({1!r} in {0!r})', operator.contains, '__contains__'
    ),
]

operator_map = {o.symbol: o for o in operators}

r_methods = [
    ('__radd__', Symbol.ADD),
    ('__rsub__', Symbol.SUB),
    ('__rmul__', Symbol.MUL),
    ('__rtruediv__', Symbol.DIV),
]
