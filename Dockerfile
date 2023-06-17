FROM python:3-alpine

WORKDIR /app

COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --dev --system --deploy

COPY . .

EXPOSE 8080

CMD [ "scrapyrt", "-i", "0.0.0.0", "-p", "8080" ]
