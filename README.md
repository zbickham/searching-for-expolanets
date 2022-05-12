# Searching for Kepler Exoplanets
This repository contains a folder with containerization scripts (`docker`), a folder with scripts to deploy the application to the cloud (`kubernetes`), a folder with the source code scripts (`src`), a folder with a test script (`test`), a text file with the required Python packages (`requirements.txt`), and a script to simplify the cycling process (`Makefile`)

## Project Summary
The objective of this project was to build a containerized Flask application for Kepler "objects of interest" and deploying it to the cloud (Kubernetes). The data being used is a cumulative record of all observed Kepler "objects of interest". The data includes information such as transit properties of the exoplanets as well as stellar properties of the stars being observed.

## Description of Files
### `docker/`
- `Dockerfile.api`: This Dockerfile contains all the commands to containerize `app.py`
- `Dockerfile.wrk`: This Dockerfile contains all the commands to conatainerize `worker.py`
- `docker-compose.yml`

### `kubernetes/`
- `prod/`
  - `app-prod-api-development.yml`: This is a file to create a deployment for the API
  - `app-prod-api-service.yml`: This is a file to generate a persistant IP address for the API
  - `app-prod-db-deployment.yml`: This is a file to create a deployment for the Redis database
  - `app-prod-db-pvc.yml`: This is a persistent volume claim file for the Redis database
  - `app-prod-db-service.yml`: This is a file to generate a persistant IP address for the Redis database
  - `app-prod-wrk-deployment.yml`: This is a file to create a deployment for the worker
- `test/`
  - `app-test-api-development.yml`: This is a file to create a test deployment for the API
  - `app-test-api-service.yml`: This is a test file to generate a persistant IP address for the API
  - `app-test-db-deployment.yml`: This is a file to create a test deployment for the Redis database
  - `app-test-db-pvc.yml`: This is a test persistent volume claim file for the Redis database
  - `app-test-db-service.yml`: This is a test file to generate a persistant IP address for the Redis database
  - `app-test-wrk-deployment.yml`: This is a file to create a test deployment for the worker

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
Next, deploy the Redis database to Kubernetes using the following commands:
```bash
$ kubectl apply -f kubernetes/prod/app-prod-db-pvc.yml
$ kubectl apply -f kubernetes/prod/app-prod-db-deployment.yml
$ kubectl apply -f kubernetes/prod/app-prod-db-service.yml
```
Once the database is deployed onto the cloud, the flask application and workers can be deployed with this command:
```bash
$ kubectl apply -f kubernete/prod/
```
This will deploy the software system on a Kubernetes cluster.

### Running the Integration Tests
To run the integration tests, enter the following command into the terminal:
```bash
$ pytest
```
This ensures that the POST, GET, PUT, and DELETE commands in the application have no errors.

### Interacting with System's CRUD Operations


### Creating a New Job
To create a new job in the application, you can run the following command:
```bash
$ curl localhost:5003/jobs -X POST
```

### Retrieving Results of a Job
After a job has finished, you can run the following command to retrieve the results:
```bash
$ curl localhost:5003/retrieve/<JOB_ID>
```

## Citations
Link for Kepler "objects of interests" CSV file: https://www.kaggle.com/datasets/nasa/kepler-exoplanet-search-results/download
