FROM python:3.12-slim as builder

ENV PATH /venv/bin:/bin:/usr/bin:/usr/local/bin
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH /code
ENV PYTHONUNBUFFERED 1
ENV PYTHONWARNINGS ignore

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked,id=apt \
    apt update

RUN --mount=type=cache,target=/root/.cache,id=pip \
    pip install -U pip uv

COPY ./requirements.txt ./code/requirements.txt

RUN python -m uv venv /venv

RUN --mount=type=cache,target=/root/.cache,id=pip \
    . /venv/bin/activate && \
    uv pip install --requirement /code/requirements.txt

WORKDIR /code

CMD ["mkdocs", "serve", "--dev-addr", "0.0.0.0:8000"]
