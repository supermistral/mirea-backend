FROM httpd:2.4

WORKDIR /usr/local/apache2/htdocs

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y \
        python3-pip \
        libexpat1 \
        libapache2-mod-wsgi-py3 \
        netcat

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r ./requirements.txt

COPY ./entrypoint.sh .
RUN chmod +x ./entrypoint.sh

ENTRYPOINT [ "/usr/local/apache2/htdocs/entrypoint.sh" ]
CMD ["httpd-foreground"]