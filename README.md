# Searching for Kepler Exoplanets
This repository contains a folder with containerization scripts (`docker`), a folder with scripts to deploy the application to the cloud (`kubernetes`), a folder with the source code scripts (`src`), a folder with a test script (`test`), a text file with the required Python packages (`requirements.txt`), and a script to simplify the cycling process (`Makefile`)

## Project Summary
The objective of this project was to build a containerized Flask application for Kepler "objects of interest" and deploying it to the cloud (Kubernetes). The data being used is a cumulative record of all observed Kepler "objects of interest". The data includes information such as transit properties of the exoplanets as well as stellar properties of the stars being observed.

## Description of Files
### `docker/`
- `Dockerfile.api`: This Dockerfile contains all the commands to containerize `app.py`
- `Dockerfile.wrk`: This Dockerfile contains all the commands to conatainerize `worker.py`
- `docker-compose.yml`

### `kubernetes/prod/`
- `app-prod-api-development.yml`: This is a file to create a deployment for the API
- `app-prod-api-service.yml`: This is a file to generate a persistant IP address for the API
- `app-prod-db-deployment.yml`: This is a file to create a deployment for the Redis database
- `app-prod-db-pvc.yml`: This is a persistent volume claim file for the Redis database
- `app-prod-db-service.yml`: This is a file to generate a persistant IP address for the Redis database
- `app-prod-wrk-deployment.yml`: This is a file to create a deployment for the worker

### `src/`

### `test/`
- `test_flask.py`: This Python script runs various unit tests to check the validity of the functions defined in the `app.py` script

### `Makefile`: This file contains commands to stop, build, and run various Docker images

### `requirements.txt`: This file contains the Python packages that are required in order to successfully run the application

## Instructions
### Deploying the Software System on a Kubernetes Cluster
To deploy the software system on a Kubernetes cluster, you first need to ssh into a k8 cluster using the following command:
```bash
$ ssh <username>@coe332-k8s.tacc.cloud
```
Once inside, clone this repository into the shell using this command:
```bash
$ git clone https://github.com/zbickham/searching-for-expolanets.git
```


### Running the Integration Tests
To run the integration tests, enter the following command into the terminal:
```bash
$ pytest
```
This ensures that the POST and GET commands in the application have no errors.

### Interacting with System's CRUD Operations

### Creating a New Job

### Retrieving Results of a Job

# Steps
1. ' wget "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=cumulative&format=csv" -O "koi_candidates.csv"'

## Citations
Link for Kepler "objects of interests" CSV file: https://www.kaggle.com/datasets/nasa/kepler-exoplanet-search-results/download
