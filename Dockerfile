# Base dependency stage
FROM python:3.12-slim as base

RUN mkdir -p /app/src app/streamlit_ui

COPY requirements-dev.txt /app/

RUN pip install --no-cache-dir -r /app/requirements-dev.txt

# API build stage
FROM base AS api

COPY src /app/src
WORKDIR /app/src

EXPOSE 5000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]

# UI build stage
FROM base AS ui

COPY streamlit_ui /app/streamlit_ui
WORKDIR /app/streamlit_ui

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.port=8501"]
