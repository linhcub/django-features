# Dockerfile
FROM python:3.10.5

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

CMD ["gunicorn", "aicore.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]