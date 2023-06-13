# Micro Ast (alpha version)

Lighweight implementation of custom AST to represent python expression structure
```
# how to represent expressions like x + 1
from uast.expression import Expr
Expr(
    Symbol.ADD,
    Expr(
        Symbol.VAR,
        'x'
    ),
    1
)  # ((x) + 1)

# but you can use automatic expression builder
from uast.builder import x
x + 1  # ((x) + 1)

# also there are short lambdas
form uast.fn import x
(x + 1)(70)  # 71
# this is roughly the same as (lambda x: x + 1)(70)
```

# TODO
- implement more operators
- implement expression matching like:  
    `match(expr=Expr(Symbol.ADD, int, int), Expr(Symbol.ADD, 2, 1))  # True`
