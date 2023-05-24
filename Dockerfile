FROM python:3.11.3

WORKDIR /app

COPY . .

RUN python -m pip install -r requirements.txt

CMD [ "scrapyrt", "-i", "0.0.0.0", "-p", "8080" ]