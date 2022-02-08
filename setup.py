from setuptools import setup

setup(
    name="example-service",
    version="0.1.2",
    install_requires=[
        "octue @ https://github.com/octue/octue-sdk-python/archive/enhancement/use-latest-apache-beam-version.zip",
    ],
    url="https://www.github.com/octue/example-service-cloud-run",
    author="cortadocodes",
    author_email="cortado.codes@protonmail.com",
    description="An example Octue service for deploying to Google Cloud Run or Google Dataflow",
)
