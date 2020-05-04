import logging
import signal

from curl_to_swagger_api.application import CurlToSwaggerApplication

logger = logging.getLogger(f'c2s.{__name__}')


def shutdown_signal_handler(signum, frame=None):
    logger.info(f'Stop cURL2Swagger application (signum: {signum}, frame: {str:{frame}}).')


signal.signal(signal.SIGTERM, shutdown_signal_handler)
signal.signal(signal.SIGINT, shutdown_signal_handler)

app = CurlToSwaggerApplication()

if __name__ == '__main__':
    app.run(port=4055, debug=False)
