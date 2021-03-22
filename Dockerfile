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

COPY ./scripts/run_analysis.py /run_analysis.py
RUN sed -i 's/\r$//g' /run_analysis.py
RUN chmod +x /run_analysis.py

EXPOSE $PORT

# Used for any environment setup that has to be done every time
#  e.g. Fetch any secrets required and (maybe?) fetch configuration files required from the store
ENTRYPOINT ["/entrypoint"]

# Script run within the entrypoint environment using the context of that environment
CMD python /run_analysis.py
