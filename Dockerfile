FROM python:3.7

COPY requirements.txt /

RUN pip install -r /requirements.txt

COPY ./curl_to_swagger /app/curl_to_swagger
COPY ./wsgi.py /app
WORKDIR /app

EXPOSE 4055

CMD gunicorn --workers $WORKERS --threads $THREADS --bind 0.0.0.0:$PORT_APP wsgi:app