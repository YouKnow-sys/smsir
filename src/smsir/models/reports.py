from pydantic import BaseModel, Field

from .status import DeliveryState


class MessageRecord(BaseModel):
    message_id: int = Field(alias="messageId")
    mobile: int = Field(alias="mobile")
    message_text: str = Field(alias="messageText")
    send_datetime: int = Field(alias="sendDateTime")
    line_number: int = Field(alias="lineNumber")
    cost: float = Field(alias="cost")
    delivery_state: DeliveryState | None = Field(alias="deliveryState")
    delivery_datetime: int | None = Field(alias="deliveryDateTime")


class PackSummary(BaseModel):
    pack_id: str = Field(alias="packId")
    recipient_count: int = Field(alias="recipientCount")
    creation_datetime: int = Field(alias="creationDateTime")
