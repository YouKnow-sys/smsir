from typing import Any

from pydantic import BaseModel, ValidationError

from .exceptions import ResponseValidationError


def parse_response[T: BaseModel](data: dict[str, Any], model: type[T]) -> T:
    try:
        return model.model_validate(data)

    except ValidationError as e:
        raise ResponseValidationError(
            f"Failed to parse response as {model.__name__}"
        ) from e
