FROM python:3.8-alpine

WORKDIR /backend
COPY requirements/production.txt /tmp/requirements

RUN pip install -r /tmp/requirements

COPY src /backend/src

EXPOSE 80
CMD ["uvicorn", "src.application:api", "--host", "0.0.0.0", "--port", "80"]
