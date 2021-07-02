from dataclasses import dataclass


@dataclass
class UriModel:
    http_method: str
    uri: str


@dataclass
class HeaderModel:
    payload: str


@dataclass
class SwaggerModel:
    payload: str
