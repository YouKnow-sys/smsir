import json as _json
from dataclasses import dataclass
from typing import Any

from ..exceptions import ResponseParsingError


@dataclass(frozen=True, slots=True)
class Response:
    status_code: int
    content: bytes

    def json(self) -> dict[str, Any]:
        if not self.content:
            raise ResponseParsingError("Empty response body", content=self.content)

        try:
            return _json.loads(self.content)
        except _json.JSONDecodeError as e:
            raise ResponseParsingError(
                f"Invalid JSON from server: {e}",
                content=self.content,
            ) from e

    @property
    def ok(self) -> bool:
        return 200 <= self.status_code < 300
