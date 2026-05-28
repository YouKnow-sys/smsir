from ..endpoints import Endpoint
from ..parser import parse_data
from ..transports import SyncTransport
from ._common import check_api_status, raise_for_status


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

    def execute[DataT](self, endpoint: Endpoint[DataT]) -> DataT:
        response = self._transport.request(
            endpoint.method,
            endpoint.build_path(),
            json=endpoint.build_body(),
            params=endpoint.build_query_params(),
        )

        raise_for_status(response)

        raw = response.json()
        check_api_status(raw, response.status_code)

        return parse_data(raw["data"], endpoint.response_model)

    def close(self):
        self._transport.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()
