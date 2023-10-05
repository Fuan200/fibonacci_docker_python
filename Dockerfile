FROM python:3.12.0-alpine3.18

WORKDIR /app

COPY . /app/

CMD [ "python", "fibo_dock.py" ]