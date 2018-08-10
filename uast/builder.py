from uast.expression import Expr
from uast.symbols import Symbol as S
from uast.symbols import operators, r_methods


class ExprBuilder(Expr):
    __slots__ = ('symbol', 'args')


def _method_factory(symbol):
    def func(self, *args):
        return type(self)(symbol, self, *args)
    return func


def _r_method_factory(symbol):
    def func(self, other):
        return type(self)(symbol, other, self)
    return func

for _operator in operators.values():
    if not _operator.method:
        continue
    setattr(ExprBuilder, _operator.method, _method_factory(_operator.symbol))

for _method, _symbol in r_methods:
    setattr(ExprBuilder, _method, _r_method_factory(_symbol))


x = ExprBuilder(S.VAR, 'x')
y = ExprBuilder(S.VAR, 'y')
z = ExprBuilder(S.VAR, 'z')
