from .operator import ConjunctionRequiredOperator, InvertableOperator, Operator


class HasMediaOperator(
    InvertableOperator[Operator],
    ConjunctionRequiredOperator,
):
    def __str__(self) -> str:
        return f"has:media"
