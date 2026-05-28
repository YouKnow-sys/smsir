from pydantic import BaseModel


class APIResponse[T](BaseModel):
    status: int
    message: str
    data: T
