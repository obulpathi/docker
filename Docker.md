# Docker

## Docker Server
* A daemon process that manages all the containers.

## Docker Client
* CLI client, which acts as a remote control for the daemon.

## Docker Hub Registry
* A cloud-based collection of docker images.

## Commands
* docker: list all sub commands
* docker search <image>: search for docker images
* docker pull <username>/<repository>: Copy a docker image to local system.
* docker images
* docker inspect
* docker run <image> <command>
* docker run --net host --cpuset 0 --memory 512mb --name chrome <image> <command>
