FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir flask

COPY registry_app.py .

EXPOSE 8000

CMD ["python", "registry_app.py"]
