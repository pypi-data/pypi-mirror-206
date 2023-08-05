from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    ForwardRef,
    List,
    Literal,
    Optional,
    Tuple,
    Type,
    TypedDict,
    Union,
    _eval_type,  # type: ignore
    get_args,
    get_origin,
)

# New in version 3.10
try:
    from typing import TypeAlias
except ImportError:
    from typing_extensions import TypeAlias

__all__ = [
    "Any",
    "Callable",
    "Dict",
    "eval_type",
    "ForwardRef",
    "get_args",
    "get_origin",
    "List",
    "Literal",
    "Optional",
    "Tuple",
    "Type",
    "TYPE_CHECKING",
    "TypedDict",
    "TypesDict",
    "Union",
]

eval_type = _eval_type
TypesDict: TypeAlias = Dict[str, Union[Optional[Type], "TypesDict"]]  # type: ignore
