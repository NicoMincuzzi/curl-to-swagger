from abc import ABC, abstractmethod

from curl_to_swagger.model.model import UrlModel, SwaggerModel


class SwaggerService(ABC):

    @abstractmethod
    def retrieve_swagger(self, endpoint_id: str) -> SwaggerModel:
        pass


class UrlService(ABC):

    @abstractmethod
    def create_url(self, url_model: UrlModel):
        pass


class HeaderService(ABC):

    @abstractmethod
    def create_header(self, base64_headers: str):
        pass


class BodyService(ABC):

    @abstractmethod
    def create_body(self, payload_model: UrlModel):
        pass
