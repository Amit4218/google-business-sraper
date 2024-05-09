FROM python:3.9-slim

ENV PYTHONUNBUFFERED   True


WORKDIR /app

COPY . ./

RUN pip install --no-cache-dir --upgrade pip 
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE $PORT


CMD exec gunicorn -b :$PORT -w 4 app:app