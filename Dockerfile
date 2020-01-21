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

<<<<<<< HEAD
CMD ["gunicorn", "--bind", "127.0.0.1:8082", "--workers", "3", "app:app"]
=======
CMD ["gunicorn", "--bind 127.0.0.1:8082","-w 3", "app:app"]
>>>>>>> 8e24edb24822ec2f33c0c7e62672540febf50550
