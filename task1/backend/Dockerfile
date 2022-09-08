FROM python:3.8-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .

RUN \
    apk add --no-cache postgresql-libs && \
    apk add --update --no-cache --virtual .build-deps gcc g++ postgresql-dev && \
    pip install -r requirements.txt --no-cache-dir --disable-pip-version-check && \
    apk del --purge .build-deps

COPY ./entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh

COPY . .

ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]