FROM python:slim-buster

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

ENV PROJECT_ROOT=/app
WORKDIR $PROJECT_ROOT

RUN apt-get update -y && \
    apt-get install -y --fix-missing \
    libpq-dev gcc git build-essential \
    && rm -rf /var/lib/apt/lists/*

# This will cache bust if any of the requirements change.
COPY requirements*.txt ./

# Upgrade to latest pip and setuptools after the cache bust, then install requirements
RUN pip install --upgrade pip && pip install -r requirements.txt


# ENTRYPOINTS AND STARTUP SCRIPTS
# ===============================

COPY ./scripts/fetch_gcloud_secrets.py /fetch_gcloud_secrets.py

COPY ./scripts/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./main.py $PROJECT_ROOT/main.py

COPY . .

EXPOSE $PORT

# Used for any environment setup that has to be done every time
# e.g. Fetch any secrets required and (maybe?) fetch configuration files required from the store
ENTRYPOINT ["/entrypoint"]

ARG _TRIGGER_ID
ENV SERVICE_ID=$_TRIGGER_ID

ARG PROJECT_ID
ENV PROJECT_ID=$_PROJECT_ID

# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD OCTUE_PATH=$(python -c "import octue; import os; print(os.path.relpath(octue.__path__[0]))") && \
    exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 "$OCTUE_PATH/deployment/google/cloud_run:app"

