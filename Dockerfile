FROM python:3.8-alpine as base
FROM base as builder
RUN mkdir /install
WORKDIR /install

COPY requirements.txt /requirements.txt
RUN pip install --install-option="--prefix=/install" -r /requirements.txt

FROM base
COPY --from=builder /install /usr/local
COPY . /app
WORKDIR /app

CMD ["gunicorn", "--bind=127.0.0.1:8082","-w 3", "app:app"]
EXPOSE 8082
