from functools import lru_cache
from typing import Any

from pydantic import TypeAdapter, ValidationError

from .exceptions import ResponseValidationError


@lru_cache(maxsize=32)
def _get_adapter(model: type) -> TypeAdapter:
    return TypeAdapter(model)


def parse_data[T](data: Any, model: type[T]) -> T:
    try:
        return _get_adapter(model).validate_python(data)
    except ValidationError as e:
        raise ResponseValidationError(
            f"Failed to parse response data as {model}"
        ) from e
