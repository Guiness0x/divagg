FROM python:3.12-alpine

WORKDIR /runtime

RUN apk add --no-cache bash postgresql-dev gcc musl-dev

RUN pip install psycopg[binary]

CMD ["sh", "/runtime/start_runtime.sh"]
