from setuptools import setup

setup(
    name="example-service",
    version="0.1.9",
    install_requires=[
        "octue@https://github.com/octue/octue-sdk-python/archive/dependencies/fix-dependency-resolution-problems.zip",
    ],
    url="https://www.github.com/octue/example-service-cloud-run",
    author="cortadocodes",
    author_email="cortado.codes@protonmail.com",
    description="An example Octue service for deploying to Google Cloud Run.",
)
