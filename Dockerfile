# Stage 1: Build environment
FROM python:3.11-slim AS builder

WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: 2000-Year Genesis Container
FROM python:3.11-slim

WORKDIR /app
COPY --from=builder /install /usr/local
COPY . /app

# Ensure non-root execution for long-term security
RUN useradd -m explorer
USER explorer

EXPOSE 8000

# Initiate the core sequence
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]