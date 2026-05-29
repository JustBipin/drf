FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# enironment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERRED=1
ENV PATH="/app/.venv/bin:$PATH"

# Omit development dependencies
ENV UV_NO_DEV=1

WORKDIR /app

COPY uv.lock pyproject.toml ./

# install project dependencies
RUN uv pip install --system . 

COPY . ./