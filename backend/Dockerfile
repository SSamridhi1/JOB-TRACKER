# Why this file exists:
# Defines a reproducible environment to run the FastAPI backend, so
# "works on my machine" isn't a problem for teammates or CI. Kept as a
# single simple stage - no multi-stage build - matching the "don't
# overengineer" instruction, since a Python API doesn't need a compiled
# build step like the frontend does.
FROM python:3.12-slim

WORKDIR /app

# Install dependencies first so Docker can cache this layer and skip
# re-installing packages every time only application code changes.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
