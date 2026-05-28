from abc import ABC
from typing import Any

from ..transports import HTTPMethod


class Endpoint[DataT](ABC):
    method: HTTPMethod
    path: str
    response_model: type[DataT]

    def build_body(self) -> dict[str, Any] | None:
        return None

    def build_query_params(self) -> dict[str, Any] | None:
        return None

    def build_path(self) -> str:
        return self.path
