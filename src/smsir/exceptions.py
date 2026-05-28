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
        response: dict | None = None,
    ):
        self.message = message
        self.status_code = status_code
        self.response = response

        super().__init__(message)

    def __str__(self) -> str:
        parts = [self.message]

        if self.status_code is not None:
            parts.append(f"status_code={self.status_code}")

        if self.response is not None:
            parts.append(f"response={self.response}")

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
