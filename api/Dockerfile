FROM python:3.11-alpine

WORKDIR /usr/src/app
RUN mkdir -p $WORKDIR/Static
RUN mkdir -p $WORKDIR/Media

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

EXPOSE 8001

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .

#ENTRYPOINT ["/usr/src/app/entrypoint.sh"]