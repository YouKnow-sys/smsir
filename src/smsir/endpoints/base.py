from abc import ABC
from typing import Any

from pydantic import BaseModel

from ..transports import HTTPMethod


class Endpoint[ResT: BaseModel](ABC):
    method: HTTPMethod
    path: str
    response_model: type[ResT]

    def build_body(self) -> dict[str, Any] | None:
        return None

    def build_query_params(self) -> dict[str, Any] | None:
        return None

    def build_path(self) -> str:
        return self.path
