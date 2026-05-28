from ..exceptions import APIError, AuthenticationError, RateLimitError
from ..models import STATUS_MESSAGES
from ..models.status import StatusCode
from ..transports import Response


def check_api_status(raw: dict, http_status: int):
    status = StatusCode(raw.get("status", 0))
    if status == StatusCode.SUCCESS:
        return

    message = raw.get("message") or STATUS_MESSAGES.get(status, "Unknown error")
    raise APIError(
        message,
        status_code=http_status,
        api_status=status,
        response=raw,
    )


def raise_for_status(response: Response):
    if response.status_code == 401:
        raise AuthenticationError(
            "Authentication failed",
            status_code=401,
        )

    if response.status_code == 429:
        raise RateLimitError(
            "Rate limited",
            status_code=429,
        )

    if response.status_code >= 400:
        try:
            data = response.json()
        except Exception:
            data = None

        raise APIError(
            "API request failed",
            status_code=response.status_code,
            response=data,
        )
