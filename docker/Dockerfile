FROM python:3.10 AS base

ENV PYTHONUNBUFFER 1
ENV PYTHONPATH /home
WORKDIR /home

COPY requirements.txt .
RUN pip3 install --no-cache-dir --upgrade -r  /home/requirements.txt

COPY .env /home/.env
COPY ./src/api /home/src/api
COPY ./src/static /home/src/static
COPY ./src/web /home/src/web
COPY ./src/ws /home/src/ws
COPY ./src/*.py /home/src/

COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh"]
CMD ["tail", "-f", "/dev/null"]