from dataclasses import dataclass


@dataclass
class UriModel:
    http_method: str = 'GET'
    uri: str = ''


@dataclass
class HeaderModel:
    headers: str


@dataclass
class BodyModel:
    id: str
    payload: str


@dataclass
class SwaggerModel:
    payload: str
