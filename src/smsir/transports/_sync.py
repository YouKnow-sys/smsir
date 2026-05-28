import httpx

from ..exceptions import NetworkError
from ._methods import HTTPMethod
from ._response import Response


class SyncTransport:
    def __init__(
        self,
        *,
        api_key: str,
        base_url: str,
        timeout: float = 20,
    ):
        self._client = httpx.Client(
            base_url=base_url,
            timeout=timeout,
            headers={
                "x-api-key": api_key,
                "Accept": "application/json",
            },
        )

    def request(
        self,
        method: HTTPMethod,
        path: str,
        *,
        json: dict[str, str] | None = None,
        params: dict[str, str] | None = None,
    ) -> Response:
        try:
            r = self._client.request(
                method,
                path,
                json=json,
                params=params,
            )
            return Response(status_code=r.status_code, content=r.content)
        except httpx.HTTPError as e:
            raise NetworkError("Request failed") from e

    def close(self):
        self._client.close()
