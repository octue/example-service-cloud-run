from setuptools import setup

setup(
    name="example-service",
    version="0.2.0",
    install_requires=[
        "octue @ https://github.com/octue/octue-sdk-python/archive/feature/add-topic-and-subscription-creation-command.zip",
    ],
    url="https://www.github.com/octue/example-service-cloud-run",
    author="cortadocodes",
    author_email="cortado.codes@protonmail.com",
    description="An example Octue service for deploying to Google Cloud Run.",
)
