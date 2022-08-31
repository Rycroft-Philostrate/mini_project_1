FROM python:3.10-slim

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
COPY utils.py .
COPY data data
COPY templates templates
COPY static static
COPY errorhandler errorhandler
COPY api api
COPY tests tests
COPY logs logs


CMD gunicorn app:app -b 0.0.0.0:80