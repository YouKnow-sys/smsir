from pydantic import BaseModel

from ..endpoints import Endpoint
from ..exceptions import APIError, AuthenticationError, RateLimitError
from ..parser import parse_response
from ..transports import Response, SyncTransport


class SMSIRClient:
    def __init__(
        self,
        api_key: str,
        *,
        base_url: str = "https://api.sms.ir/v1",
        timeout: float = 20,
    ):
        self._transport = SyncTransport(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
        )

    def execute[ResT: BaseModel](self, endpoint: Endpoint[ResT]) -> ResT:
        response = self._transport.request(
            endpoint.method,
            endpoint.build_path(),
            json=endpoint.build_body(),
            params=endpoint.build_query_params(),
        )

        self._raise_for_status(response)

        data = response.json()

        return parse_response(
            data,
            endpoint.response_model,
        )

    def _raise_for_status(self, response: Response):
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

    def close(self):
        self._transport.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()
