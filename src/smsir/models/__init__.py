from .base import APIResponse
from .receive import ReceivedMessage, ReceivedMessageWithId
from .reports import MessageRecord, PackSummary
from .send import BulkSendData, CancelScheduledData, VerifySendData

BulkSendResponse = APIResponse[BulkSendData]
VerifySendResponse = APIResponse[VerifySendData]
SendByURLResponse = APIResponse[VerifySendData]
CancelScheduledResponse = APIResponse[CancelScheduledData]
MessageReportResponse = APIResponse[MessageRecord]
PackListResponse = APIResponse[list[PackSummary]]
PackReportResponse = APIResponse[list[MessageRecord]]
LiveSendResponse = APIResponse[list[MessageRecord]]
ArchiveSendResponse = APIResponse[list[MessageRecord]]
LatestReceiveResponse = APIResponse[list[ReceivedMessageWithId]]
LiveReceiveResponse = APIResponse[list[ReceivedMessage]]
ArchiveReceiveResponse = APIResponse[list[ReceivedMessageWithId]]
CreditResponse = APIResponse[float]
LinesResponse = APIResponse[list[int]]

__all__ = [
    "BulkSendResponse",
    "VerifySendResponse",
    "SendByURLResponse",
    "CancelScheduledResponse",
    "MessageReportResponse",
    "PackListResponse",
    "PackReportResponse",
    "LiveSendResponse",
    "ArchiveSendResponse",
    "LatestReceiveResponse",
    "LiveReceiveResponse",
    "ArchiveReceiveResponse",
    "CreditResponse",
    "LinesResponse",
]
