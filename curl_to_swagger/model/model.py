from dataclasses import dataclass
from typing import Optional


@dataclass
class UriModel:
    http_method: str = 'GET'
    uri: str = ''


@dataclass
class HeaderModel:
    id: str
    headers: str


@dataclass
class BodyModel:
    id: str
    payload: Optional[str]


@dataclass
class SwaggerModel:
    payload: str
