# FastAPI and Docker Try-out

## Fast API
FastAPI is a modern, fast web framework for building APIs with Python 3.7+.

## Docker
Docker is an open-source platform that automates the deployment, scaling, and management of applications in containers.
| Command             | Description                                                                     |Example                                       |
|-------------------- |---------------------------------------------------------------------------------|----------------------------------------------|
| **`docker images`** | Lists all the images on local.                                                  | `docker images`                              |
| **`docker rmi`**    | Removes one or more images from local.                                          | `docker rmi <image_name>`                    |
| **`docker rm`**     | Removes one or more stopped containers.                                         | `docker rm <container_id>`                   |
| **`docker ps -a`**  | Lists all containers (running and stopped).                                     | `docker ps -a`                               |
| **`docker pull`**   | Pulls an image from a Docker registry (e.g., Docker Hub).                       | `docker pull <image_name>`                   |
| **`docker build`**  | Builds an image from a Dockerfile in the current directory.                     | `docker build -t <image_name> .`             |
| **`docker run`**    | Creates and starts a container from an image. Can expose ports and map volumes. | `docker run -p 8000:8000 <image_name>`       |

```
docker pull python:3.12-slim 
docker run --rm -it python:3.12-slim /bin/bash
docker run --rm -it --entrypoint=/bin/bash -v F:/docker-test:/workspace python:3.12-slim  
```

## Repo Explaination 
| File Name              | Description                                                                      |
|------------------------|----------------------------------------------------------------------------------|
| **`Dockerfile`**       | Contains instructions to build the Docker image for the project                  |
| **`fastAPI.py`**       | The main FastAPI application file that defines your API endpoints and logic.     |
| **`send.py`**          | A Python script to call the deployed APIs.                                       |
| **`requirements.txt`** | lists all the Python dependencies |
