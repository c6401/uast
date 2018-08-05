from uast.builder import ExprBuilder
from uast.expression import Expr
from uast.symbols import Symbol as S, operators

from typing import Callable, Any

MYPY = False
if MYPY:
    ULambdaType = Callable[[dict], Any]


def translate_expression(expression):  # type: (Expr) -> ULambdaType
    if expression.symbol == S.VAR:
        return lambda scope: scope[expression.args[0]]

    args = [translate(arg) for arg in expression.args]
    return lambda scope: operators[
        expression.symbol
    ].operator(*(a(scope) for a in args))


def translate_list(list_):  # type: (list) -> ULambdaType
    items = [translate(i) for i in list_]
    return lambda scope: [i(scope) for i in items]


def translate_tuple(tuple_):  # type: (tuple) -> ULambdaType
    items = [translate(i) for i in tuple_]
    return lambda scope: tuple(i(scope) for i in items)


def translate_dict(dict_):  # type: (dict) -> ULambdaType
    items = [(k, translate(v)) for k, v in dict_.items()]
    return lambda scope: {k: v(scope) for k, v in items}


def translate(expression):  # type: (Expr) -> ULambdaType
    if isinstance(expression, Expr):
        return translate_expression(expression)
    elif isinstance(expression, list):
        return translate_list(expression)
    elif isinstance(translate, tuple):
        return translate_tuple(expression)
    elif isinstance(expression, dict):
        return translate_dict(expression)
    return lambda scope: expression


def run(expression, x=None, y=None, z=None, **scope):
        if x:
            scope.update(x=x)
        if y:
            scope.update(y=y)
        if z:
            scope.update(z=z)
        return translate(expression)(scope)


class Lambda(ExprBuilder):
    def __call__(self, x=None, y=None, z=None, **scope):
        return run(self, x, y, x, **scope)


x = Lambda(S.VAR, 'x')
y = Lambda(S.VAR, 'y')
z = Lambda(S.VAR, 'z')
