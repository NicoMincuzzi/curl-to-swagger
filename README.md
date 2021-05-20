# cURL 2 Swagger

![PyPI - Python Version](https://img.shields.io/badge/python-3.6%7C3.7%7C3.8-blue) [![Version](https://img.shields.io/badge/version-v0.1.0-green)](https://github.com/NicoMincuzzi/curl-to-swagger) ![GitHub repo size](https://img.shields.io/github/repo-size/NicoMincuzzi/curl-to-swagger)

docker build -t c2s:latest .

docker container run -e "WORKERS=4" -e "THREADS=4" -e "PORT_APP=4055" -p 4055:4055 c2s:latest
