from abc import ABC, abstractmethod

from curl_to_swagger_core.model.model import PayloadModel, SwaggerModel, CurlModel


class ConverterService(ABC):

    @abstractmethod
    def convert_to_curl(self, payload_model: PayloadModel) -> CurlModel:
        pass

    @abstractmethod
    def convert_to_swagger(self, curl_model: CurlModel) -> SwaggerModel:
        pass
