FROM python:3.7

COPY requirements.txt /

RUN pip install -r /requirements.txt

COPY ./application/src /app
WORKDIR /app

CMD gunicorn --workers $WORKERS --threads $THREADS --bind 0.0.0.0:$PORT_APP wsgi:app