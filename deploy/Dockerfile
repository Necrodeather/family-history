FROM python:3.12.9-slim-bookworm

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1
    PYTHONPATH=app

ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100


WORKDIR /app

RUN pip install --upgrade pip \
    && pip install uv

COPY . .
RUN uv pip install -r pyproject.toml --system

CMD ["python", "app/main.py"]