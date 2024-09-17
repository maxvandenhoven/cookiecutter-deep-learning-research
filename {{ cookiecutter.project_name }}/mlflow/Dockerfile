# Use simple Python base image (version is not parameterized as it doesn't really matter).
FROM python:3.10-slim-buster

# Install specified MLflow version (defaults to 2.9.2 for old-school tracking interface).
ARG MLFLOW_VERSION=2.9.2
RUN pip install mlflow${MLFLOW_VERSION:+==${MLFLOW_VERSION}}

# Expose port 5000 to serve MLflow web interface.
EXPOSE 5000