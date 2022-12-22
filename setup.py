from setuptools import setup


setup(
    name="example-service",
    version="0.2.0",
    install_requires=[
        "octue==0.43.2",
        "pre-commit>=2.20.0",
    ],
    url="https://www.github.com/octue/example-service-cloud-run",
    author="Marcus Lugg",
    author_email="marcus@octue.com",
    description="An example Octue service for deploying to Google Cloud Run.",
)
