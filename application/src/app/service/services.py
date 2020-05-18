from abc import ABC, abstractmethod

from app.model.model import PayloadModel, CurlModel, SwaggerModel


class ConverterService(ABC):

    @abstractmethod
    def convert_to_curl(self, payload_model: PayloadModel) -> CurlModel:
        pass

    @abstractmethod
    def convert_to_swagger(self, curl_model: CurlModel) -> SwaggerModel:
        pass
