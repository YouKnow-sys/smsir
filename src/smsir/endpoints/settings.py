from dataclasses import dataclass

from ..models import CreditResponse, LinesResponse
from ..transports import HTTPMethod
from .base import Endpoint


@dataclass(slots=True, kw_only=True)
class GetCredit(Endpoint[CreditResponse]):
    method = HTTPMethod.GET
    path = "/credit"
    response_model = CreditResponse


@dataclass(slots=True, kw_only=True)
class GetLines(Endpoint[LinesResponse]):
    method = HTTPMethod.GET
    path = "/line"
    response_model = LinesResponse
