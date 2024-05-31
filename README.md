# About

This is simple project with the aim to test GitHub actions pipeline to build and deploy simple Flask application on Azure Container Apps.

## Build

Run Docker to build: `docker build -t flask-gunicorn-boilerplate:latest .`

Docker to run: `docker run -p 8000:8000 flask-gunicorn-boilerplate:latest`