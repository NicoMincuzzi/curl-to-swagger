from curl_to_swagger.model.model import SwaggerModel
from curl_to_swagger.service.services import SwaggerService


class SwaggerServiceImpl(SwaggerService):

    def retrieve_swagger(self, endpoint_id: str) -> SwaggerModel:
        pass
