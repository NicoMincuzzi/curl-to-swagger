from curl_to_swagger_core.service import ConverterService

from curl_to_swagger_core.model.model import PayloadModel, CurlModel


class ConverterServiceImpl(ConverterService):

    def convert_to_curl(self, payload_model: PayloadModel) -> CurlModel:
        pass
