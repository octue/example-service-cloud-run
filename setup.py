from setuptools import setup

setup(
    name="example-service",
    version="0.1.1",
    install_requires=[
        "octue==0.9.1",
    ],
    url="https://www.github.com/octue/example-service-cloud-run",
    author="cortadocodes",
    author_email="cortado.codes@protonmail.com",
    description="An example Octue service for deploying to Google Cloud Run or Google Dataflow",
)
