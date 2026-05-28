from pydantic import BaseModel, Field


class ReceivedMessage(BaseModel):
    mobile: int = Field(alias="mobile")
    message_text: str = Field(alias="messageText")
    number: int = Field(alias="number")
    received_datetime: int = Field(alias="receivedDateTime")


class ReceivedMessageWithId(ReceivedMessage):
    receive_return_id: int = Field(alias="receiveReturnId")
