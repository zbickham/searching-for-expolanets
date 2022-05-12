# Searching for Kepler Exoplanets
This repository contains a folder with containerization scripts (`docker`), a folder with scripts to deploy the application to the cloud (`kubernetes`), a folder with the source code scripts (`src`), a folder with a test script (`test`), a text file with the required Python packages (`requirements.txt`), and a script to simplify the cycling process (`Makefile`)

## Project Summary
The objective of this project was to build a containerized Flask application for Kepler "objects of interest" and deploying it to the cloud (Kubernetes). The data being used is a cumulative record of all observed Kepler "objects of interest". The data includes information such as transit properties of the exoplanets as well as stellar properties of the stars being observed.

## Description of Files
### `docker/`
#### `Dockerfile.api`
#### `Dockerfile.wrk`
#### `docker-compose.yml`

### kubernetes/prod
#### `app-prod-api-development.yml`
#### `app-prod-api-service.yml`
#### `app-prod-db-deployment.yml`
#### `app-prod-db-pvc.yml`
#### `app-prod-db-service.yml`
#### `app-prod-wrk-deployment.yml`

### src

### test/
#### test_flask.py


## Instructions
### Deploying the Software System on a Kubernetes Cluster


### Running the Integration Tests

### Interacting with System's CRUD Operations

### Creating a New Job

### Retrieving Results of a Job

# Steps
1. ' wget "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=cumulative&format=csv" -O "koi_candidates.csv"'

## Citations
