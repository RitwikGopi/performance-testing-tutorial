
FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt


# Use the OpenTelemetry launcher to auto-instrument the app
CMD ["gunicorn", "-b", "0.0.0.0:5000", "--workers=1", "--threads=1", "--capture-output", "--access-logfile", "-", "app:app"]
