from dataclasses import dataclass


@dataclass
class PayloadModel:
    payload: str


@dataclass
class CurlModel:
    payload: str


@dataclass
class SwaggerModel:
    payload: str
