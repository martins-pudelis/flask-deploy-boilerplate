# About

This is simple project with the aim to test GitHub actions pipeline to build and deploy simple Flask application on Azure Container Apps. 

Currently it builds Docker image and pushes it to the Docker hub and afterwards Azure pulls image from repozitory and deploys image as Azure container app. Image can be stored also in Azure repozitory (or any other), but it comes with the extra costs and for POC project there are rather low requirements for privacy, therefore Docker Hub public repository is perfect option.

For now revision in Azure is created manually to have some control for the deployment, but it also can be automated, however then better would be build Docker image on release, instead of each push.

## Prerequisites

Automated build:
1. Docker hub repository, with registered token
2. Registered secrets for the GithHub repository
3. Workflow with the custome image name (configured in workflow yml file)

Azure deployment:
1. Azure Subscription
2. New or existing resource group
3. New Azure container app with according image repository loacation and name

## Local build

To build and run Docker images use commands bellow:

* Run Docker to build: `docker build -t flask-gunicorn-boilerplate:latest .`
* Docker to run: `docker run -p 8000:8000 flask-gunicorn-boilerplate:latest`
