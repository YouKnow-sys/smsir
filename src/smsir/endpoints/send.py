from dataclasses import dataclass
from datetime import datetime

from ..models import (
    BulkSendResponse,
    CancelScheduledResponse,
    SendByURLResponse,
    VerifySendResponse,
)
from ..transports import HTTPMethod
from ..utils import to_unix
from .base import Endpoint


@dataclass(slots=True, kw_only=True)
class BulkSend(Endpoint[BulkSendResponse]):
    line_number: int
    message_text: str
    mobiles: list[str]
    send_datetime: datetime | None = None

    method = HTTPMethod.POST
    path = "/send/bulk"
    response_model = BulkSendResponse

    def build_body(self):
        body = {
            "lineNumber": self.line_number,
            "messageText": self.message_text,
            "mobiles": self.mobiles,
        }
        if self.send_datetime is not None:
            body["sendDateTime"] = to_unix(self.send_datetime)
        return body


@dataclass(slots=True, kw_only=True)
class LikeToLikeSend(Endpoint[BulkSendResponse]):
    line_number: int
    message_texts: list[str]
    mobiles: list[str]
    send_datetime: datetime | None = None

    method = HTTPMethod.POST
    path = "/send/likeToLike"
    response_model = BulkSendResponse

    def build_body(self):
        body = {
            "lineNumber": self.line_number,
            "messageTexts": self.message_texts,
            "mobiles": self.mobiles,
        }
        if self.send_datetime is not None:
            body["sendDateTime"] = to_unix(self.send_datetime)
        return body


@dataclass(slots=True, kw_only=True)
class VerifySend(Endpoint[VerifySendResponse]):
    mobile: str
    template_id: int
    parameters: dict[str, str]

    method = HTTPMethod.POST
    path = "/send/verify"
    response_model = VerifySendResponse

    def build_body(self):
        return {
            "mobile": self.mobile,
            "templateId": self.template_id,
            "parameters": [
                {"name": name, "value": value}
                for name, value in self.parameters.items()
            ],
        }


@dataclass(slots=True, kw_only=True)
class CancelScheduledSend(Endpoint[CancelScheduledResponse]):
    pack_id: str

    method = HTTPMethod.DELETE
    path = "/send/scheduled/{pack_id}"
    response_model = CancelScheduledResponse

    def build_path(self):
        return self.path.format(pack_id=self.pack_id)


@dataclass(slots=True, kw_only=True)
class SendByURL(Endpoint[SendByURLResponse]):
    username: str
    password: str
    line: int
    mobile: str
    text: str

    method = HTTPMethod.GET
    path = "/send"
    response_model = SendByURLResponse

    def build_query_params(self):
        return {
            "username": self.username,
            "password": self.password,
            "line": self.line,
            "mobile": self.mobile,
            "text": self.text,
        }
