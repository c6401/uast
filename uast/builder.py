from uast.expression import Expr
from uast.symbols import Symbol as S, operators


class ExprBuilder(Expr):
    __slots__ = ('symbol', 'args')


for _operator in operators.values():
    if not _operator.method:
        continue

    def func_factory():
        operator = _operator

        def func(self, *args):
            return type(self)(operator.symbol, self, *args)

        func.__name__ = operator.method
        return func

    setattr(ExprBuilder, _operator.method, func_factory())


x = ExprBuilder(S.VAR, 'x')
y = ExprBuilder(S.VAR, 'y')
z = ExprBuilder(S.VAR, 'z')
