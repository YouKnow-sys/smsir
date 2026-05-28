from pydantic import BaseModel, Field


class BulkSendData(BaseModel):
    pack_id: str = Field(alias="packId")
    message_ids: list[int | None] = Field(alias="messageIds")
    cost: float = Field(alias="cost")


class VerifySendData(BaseModel):
    message_id: int = Field(alias="messageId")
    cost: float = Field(alias="cost")


class CancelScheduledData(BaseModel):
    returned_credit_count: float = Field(alias="returnedCreditCount")
    sms_count: int = Field(alias="smsCount")
