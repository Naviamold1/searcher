FROM python:3-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8080

CMD [ "scrapyrt", "-i", "0.0.0.0", "-p", "8080" ]
