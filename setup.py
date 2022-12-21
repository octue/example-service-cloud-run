from setuptools import setup

setup(
    name="example-service",
    version="0.2.0",
    install_requires=[
        "octue @ https://github.com/octue/octue-sdk-python/archive/devops/improve-deployment-dockerfile.zip",
    ],
    url="https://www.github.com/octue/example-service-cloud-run",
    author="Marcus Lugg",
    author_email="marcus@octue.com",
    description="An example Octue service for deploying to Google Cloud Run.",
)
