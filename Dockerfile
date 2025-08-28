FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    jq \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir nibabel

COPY main.py main main.yaml /app/
RUN chmod +x /app/main

CMD ["/app/main"]
