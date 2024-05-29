# intelligent-meter

## Description

This folder contains the application service to run the backend service. It is developed using FastAPI in Python.

## Prerequisites

### Python
This project was developed in `Python 3.10.14`. So for the best of interest, please use the same version to avoid any issues.

The official binary installer for `Python 3.10.14` is not publicly available anymore due to their policy. Here you have two options:

#### Install via Miniconda (**Recommended**)
- These installers are easier to manage, and handle most things for you.
- Download and install Miniconda [here](https://docs.anaconda.com/free/miniconda/miniconda-other-installer-links/)


#### Install through third-party providers

- There are repositories that keep all the released binary installers
- Might be untrustworthy as they might be tampered with

### Dependencies

The requirements for the project can be found in the `requirements.txt` file. 

#### Detailed steps (Using Miniconda)

1. Search and run `Anaconda Prompt (miniconda3)` program from Windows Search
2. (Optional) Create a virtual environment `conda create --name <env-name> python=3.10.14`
3. (Optional) Activate the new environment `conda activate <env-name>`
4. Navigate to the project directory `cd <path/to/project>`
5. Execute `pip install -r requirements.txt`

## Running the server

The installed dependencies should come with uvicorn, an ASGI web server. You can use this to simply start the server.

```bash
uvicorn main:app
```

By default the port is 8000, but you can change the port by adding the `--port` flag.

Example:

```bash
uvicorn main:app --port 9090
```

To stop the server, just hit `CTRL+C`.

## Documentation

### Swagger UI & ReDoc

The whole project is partially auto-documented in `Swagger UI` and `ReDoc`. Once the server is running, you can visit
- http://localhost:8000/docs (Swagger UI)
- http://localhost:8000/redoc (ReDoc)

### OpenAPI

An OpenAPI-compliant schema is also generated at http://127.0.0.1:8000/openapi.json


## Unit tests

To be implemented.
