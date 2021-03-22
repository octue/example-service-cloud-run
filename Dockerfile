FROM python:slim-buster

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

# If setup.py exists
#RUN pip install -e .


# ENTRYPOINTS AND STARTUP SCRIPTS
# ===============================

COPY ./scripts/fetch_gcloud_secrets.py /fetch_gcloud_secrets.py

COPY ./scripts/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./main.py $PROJECT_ROOT/main.py

COPY . .

EXPOSE $PORT

ARG _TRIGGER_ID
ARG PROJECT_ID

# Used for any environment setup that has to be done every time
#  e.g. Fetch any secrets required and (maybe?) fetch configuration files required from the store
ENTRYPOINT ["/entrypoint"]

# Script run within the entrypoint environment using the context of that environment

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
