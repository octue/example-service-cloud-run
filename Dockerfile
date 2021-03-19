FROM python:slim-buster

# Set the application root directory
ENV PROJECT_ROOT=/app
WORKDIR $PROJECT_ROOT

# Dependencies for building python dependencies.... do we need?
#RUN apt-get update -y && \
#    apt-get install -y --fix-missing \
#    libpq-dev gcc git \
#    && rm -rf /var/lib/apt/lists/*

# This will cache bust if any of the requirements files change
COPY requirements*.txt ./

# Upgrade to latest pip and setuptools after the cache bust, then install requirements
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# If setup.py exists
#RUN pip install -e .


# ENTRYPOINTS AND STARTUP SCRIPTS
# ===============================

COPY ./compose/scripts/fetch_gcloud_secrets.py /fetch_gcloud_secrets.py
COPY ./compose/scripts/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/scripts/run-analysis /run-analysis
RUN sed -i 's/\r$//g' /run-analysis
RUN chmod +x /run-analysis

# Used for any environment setup that has to be done every time
#  e.g. Fetch any secrets required and (maybe?) fetch configuration files required from the store
ENTRYPOINT ["/entrypoint"]

# Script run within the entrypoint environment using the context of that environment
CMD /run-analysis
