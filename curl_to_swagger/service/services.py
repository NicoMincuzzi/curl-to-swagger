from abc import ABC, abstractmethod

from curl_to_swagger.model.model import PayloadModel, CurlModel, SwaggerModel


class SwaggerService(ABC):

    @abstractmethod
    def retrieve_swagger(self, endpoint_id: str) -> SwaggerModel:
        pass


class UrlService(ABC):

    @abstractmethod
    def create_url(self, payload_model: PayloadModel) -> CurlModel:
        pass


class HeaderService(ABC):

    @abstractmethod
    def create_header(self, payload_model: PayloadModel) -> CurlModel:
        pass


class BodyService(ABC):

    @abstractmethod
    def create_body(self, payload_model: PayloadModel) -> CurlModel:
        pass
