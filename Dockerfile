FROM python:3.11-slim

RUN adduser --disabled-password --gecos "" appuser

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

COPY blog_app/ blog_app/
COPY migrations/ migrations/
COPY alembic.ini .

RUN echo '#!/bin/bash\nalembic upgrade head\npython -m blog_app.seed\nuvicorn blog_app.main:app --host 0.0.0.0 --port 8000' > /app/start.sh \
    && chmod +x /app/start.sh

RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

CMD ["/app/start.sh"]
