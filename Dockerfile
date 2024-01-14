FROM python:3.10.12-alpine
WORKDIR /usr/src/api
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependiencies
RUN python3 -m pip install --upgrade pip
RUN apk add --no-cache postgresql-libs curl
RUN apk add --no-cache --virtual .build-deps zlib-dev jpeg-dev gcc musl-dev postgresql-dev
COPY ./requirements/base.txt ./requirements.txt
RUN \
  python3 -m pip install -r requirements.txt --no-cache-dir && \
  apk --purge del .build-deps
COPY . .
