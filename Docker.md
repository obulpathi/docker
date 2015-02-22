# Docker

## Docker Server
* A daemon process that manages all the containers.

## Docker Client
* CLI client, which acts as a remote control for the daemon.

## Docker Hub Registry
* A cloud-based collection of docker images.

## Vocabulary
* image: a blueprint for a system
* container: an instantiation of a docker image

## Commands
* docker: list all sub commands
* docker help: invoke docker help subcommand
* docker help <subcommand>: invoke docker help on subcommand
* docker search <image>: search for docker images
* docker pull <username>/<repository>: Copy a docker image to local system.
* docker images: list docker images
* docker rmi <image>: remove docker image
* docker run help
* docker run <image> <command>
* docker run --name <name> <image> <command>: assign name to container
* docker run -i/--interactive <image> <command>: run container in interactive mode
* docker run -d/--detach <image> <command>: run container in daemon mode
* docker run -m/--memory <memory> <image> <command>: limit containers memory
* docker run --cpuset <cpus> <image> <command>: run container on assigned CPUs
* docker run --device /dev/sdc:/dev/xvdc <image> <command>: run container with attached volume
* docker run -v /host:/container <image> <command>: mount volume in container
* docker run --net bridge/host <image> <command>: run container in
* docker run --net host --cpuset 0 --memory 512mb --name mycontainer <image> <command>
* docker ps: show running containers
* docker ps -a: show all containers
* docker rm <container>: remove docker container
* docker inspect <container>: return low level info about container
* docker attach <container>: attach to a running container
* docker pause <container>: pause a container
* docker unpause <container>: unpause a paused container
* docker stop <container>: gracefully stop a container (send SIGTERM, then SIGKILL)
* docker kill <container>: kill the process in container using SIGKILL
* docker restart <container>: restart a running container
* docker cp <container>:<path> <hostpath>
