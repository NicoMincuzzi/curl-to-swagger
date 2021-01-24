docker build -t c2s:latest .

docker container run -e "WORKERS=4" -e "THREADS=4" -e "PORT_APP=4055" -p 4055:4055 c2s:latest