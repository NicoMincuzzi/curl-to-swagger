from dataclasses import dataclass


@dataclass
class UrlModel:
    http_method: str
    url: str


@dataclass
class HeaderModel:
    payload: str


@dataclass
class SwaggerModel:
    payload: str
