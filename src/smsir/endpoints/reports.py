from dataclasses import dataclass
from datetime import datetime

from ..models import (
    MessageRecord,
    PackSummary,
    ReceivedMessage,
    ReceivedMessageWithId,
)
from ..transports import HTTPMethod
from ..utils import to_unix
from .base import Endpoint


@dataclass(slots=True, kw_only=True)
class MessageReport(Endpoint[MessageRecord]):
    message_id: int

    method = HTTPMethod.GET
    path = "/send/{message_id}"
    response_model = MessageRecord

    def build_path(self):
        return self.path.format(message_id=self.message_id)


@dataclass(slots=True, kw_only=True)
class PackListReport(Endpoint[list[PackSummary]]):
    page_size: int | None = None
    page_number: int | None = None

    method = HTTPMethod.GET
    path = "/send/pack"
    response_model = list[PackSummary]

    def build_query_params(self):
        params: dict[str, int] = {}
        if self.page_size is not None:
            params["pageSize"] = self.page_size
        if self.page_number is not None:
            params["pageNumber"] = self.page_number
        return params or None


@dataclass(slots=True, kw_only=True)
class PackReport(Endpoint[list[MessageRecord]]):
    pack_id: str

    method = HTTPMethod.GET
    path = "/send/pack/{pack_id}"
    response_model = list[MessageRecord]

    def build_path(self):
        return self.path.format(pack_id=self.pack_id)


@dataclass(slots=True, kw_only=True)
class LiveSendReport(Endpoint[list[MessageRecord]]):
    page_size: int | None = None
    page_number: int | None = None

    method = HTTPMethod.GET
    path = "/send/live"
    response_model = list[MessageRecord]

    def build_query_params(self):
        params: dict[str, int] = {}
        if self.page_size is not None:
            params["pageSize"] = self.page_size
        if self.page_number is not None:
            params["pageNumber"] = self.page_number
        return params or None


@dataclass(slots=True, kw_only=True)
class ArchiveSendReport(Endpoint[list[MessageRecord]]):
    from_date: datetime | None = None
    to_date: datetime | None = None
    page_size: int | None = None
    page_number: int | None = None

    method = HTTPMethod.GET
    path = "/send/archive"
    response_model = list[MessageRecord]

    def build_query_params(self):
        params: dict[str, int] = {}
        if self.from_date is not None:
            params["fromDate"] = to_unix(self.from_date)
        if self.to_date is not None:
            params["toDate"] = to_unix(self.to_date)
        if self.page_size is not None:
            params["pageSize"] = self.page_size
        if self.page_number is not None:
            params["pageNumber"] = self.page_number
        return params or None


@dataclass(slots=True, kw_only=True)
class LatestReceive(Endpoint[list[ReceivedMessageWithId]]):
    count: int | None = None

    method = HTTPMethod.GET
    path = "/receive/latest"
    response_model = list[ReceivedMessageWithId]

    def build_query_params(self):
        if self.count is not None:
            return {"count": self.count}
        return None


@dataclass(slots=True, kw_only=True)
class LiveReceive(Endpoint[list[ReceivedMessage]]):
    page_size: int | None = None
    page_number: int | None = None
    sort_by_newest: bool | None = None

    method = HTTPMethod.GET
    path = "/receive/live"
    response_model = list[ReceivedMessage]

    def build_query_params(self):
        params: dict[str, int | bool] = {}
        if self.page_size is not None:
            params["pageSize"] = self.page_size
        if self.page_number is not None:
            params["pageNumber"] = self.page_number
        if self.sort_by_newest is not None:
            params["sortByNewest"] = self.sort_by_newest
        return params or None


@dataclass(slots=True, kw_only=True)
class ArchiveReceive(Endpoint[list[ReceivedMessageWithId]]):
    from_date: datetime | None = None
    to_date: datetime | None = None
    page_size: int | None = None
    page_number: int | None = None

    method = HTTPMethod.GET
    path = "/receive/archive"
    response_model = list[ReceivedMessageWithId]

    def build_query_params(self):
        params: dict[str, int] = {}
        if self.from_date is not None:
            params["fromDate"] = to_unix(self.from_date)
        if self.to_date is not None:
            params["toDate"] = to_unix(self.to_date)
        if self.page_size is not None:
            params["pageSize"] = self.page_size
        if self.page_number is not None:
            params["pageNumber"] = self.page_number
        return params or None
