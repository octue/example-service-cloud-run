FROM apache/beam_python3.8_sdk:2.35.0

# Allow statements and log messages to immediately appear in the logs on Google Cloud.
ENV PYTHONUNBUFFERED=1

ENV PROJECT_ROOT=/app
WORKDIR $PROJECT_ROOT

RUN apt-get update -y && apt-get install -y --fix-missing build-essential && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

ENV USE_OCTUE_LOG_HANDLER=1
ENV COMPUTE_PROVIDER=GOOGLE_CLOUD_RUN

ENV SERVICE_ID=octue.services.1df81225-7e87-4b1c-9413-cdc375a127a7
