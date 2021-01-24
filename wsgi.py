import logging
import signal

from curl_to_swagger.application import CurlToSwaggerApplication

logger = logging.getLogger(f'c2s.{__name__}')


def shutdown_signal_handler(signum, frame=None):
    logger.info(f'Stop cURL2Swagger application (signum: {signum}, frame: {str:{frame}}).')


# with open(os.path.join(os.path.dirname(__file__), 'config', 'logo.txt')) as logo_file:
#    logger.info(logo_file.read())

signal.signal(signal.SIGTERM, shutdown_signal_handler)
signal.signal(signal.SIGINT, shutdown_signal_handler)

app = CurlToSwaggerApplication()

if __name__ == '__main__':
    app.run(port=4055, debug=False)
