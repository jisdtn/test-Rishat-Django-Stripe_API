FROM python:3.10

COPY get_random_secret_key.sh get_random_secret_key.sh

WORKDIR /payment_forms

RUN pip3 freeze > requirements.txt

COPY . .

RUN pip3 install -r requirements.txt --no-cache-dir