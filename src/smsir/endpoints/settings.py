from dataclasses import dataclass

from ..transports import HTTPMethod
from .base import Endpoint


@dataclass(slots=True, kw_only=True)
class GetCredit(Endpoint[float]):
    method = HTTPMethod.GET
    path = "/credit"
    response_model = float


@dataclass(slots=True, kw_only=True)
class GetLines(Endpoint[list[int]]):
    method = HTTPMethod.GET
    path = "/line"
    response_model = list[int]
