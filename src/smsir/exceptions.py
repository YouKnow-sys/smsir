from __future__ import annotations

from .models.status import StatusCode


class SMSIRError(Exception):
    pass


class NetworkError(SMSIRError):
    pass


class APIError(SMSIRError):
    def __init__(
        self,
        message: str,
        *,
        status_code: int | None = None,
        api_status: StatusCode | None = None,
        response: dict | None = None,
    ):
        self.message = message
        self.status_code = status_code
        self.api_status = api_status
        self.response = response

        super().__init__(message)

    def __str__(self) -> str:
        parts = [self.message]

        if self.api_status is not None:
            parts.append(f"api_status={self.api_status.name}({self.api_status.value})")

        if self.status_code is not None:
            parts.append(f"http_status={self.status_code}")

        return " | ".join(parts)


class AuthenticationError(APIError):
    pass


class RateLimitError(APIError):
    pass


class ResponseParsingError(SMSIRError):
    def __init__(self, message: str, *, content: bytes):
        self.content = content
        super().__init__(message)


class ResponseValidationError(SMSIRError):
    pass
