# Docker

## Vocabulary
* docker image: a blueprint for a lightweight virtual machine (Class)
* docker container: an instantiation of a docker image (Object)

## Docker Server
* A daemon process that manages all the containers.

## Docker Client
* CLI client, which acts as a remote control for the daemon.

## Docker Hub Registry
* A cloud-based collection of docker images.

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

## Dockerfile
* A Dockerfile is a text document that contains all the commands required to build a Docker image
* By calling "docker build" from your terminal, you can have Docker build your image
* docker build -t <username>/<imagename> <dir>: build a docker image
* The path to the source repository defines where to find the context of the build
* The build is run by the Docker daemon, not by the CLI, so the whole context must be transferred to the daemon
* Once the image is built, it can be pushed to the DockerHub repository using "docker push"
* docker push <username>/<imagename>: push the image to DockerHub repository

### Dockerfile commands

#### Comments
* Comments start with '#'

#### ADD
* Usage: ADD [source directory or URL] [destination directory]
* Copies the files from the source into the container

#### CMD
* The command CMD is used for executing a specific command.
* The command will be executed a container is instantiated using the image being built.
* Usage: CMD application "argument", "argument", ..
* Example: CMD "echo" "Hello docker!"

#### ENTRYPOINT
* ENTRYPOINT argument sets the concrete default application that is used every time a container is created using the image.
* For example, if you have installed a specific application inside an image and you will use this image to only run that application, you can state it with ENTRYPOINT and whenever a container is created from that image, your application will be the target.
* If you couple ENTRYPOINT with CMD, you can remove "application" from CMD and just leave "arguments" which will be passed to the ENTRYPOINT.
* Usage: ENTRYPOINT application "argument", "argument", ..
* Example: CMD "Hello docker!"
* Example: ENTRYPOINT echo  

#### ENV
* The ENV command is used to set the environment variables (one or more).
* These variables consist of “key = value” pairs which can be accessed within the container by scripts and applications alike.
* This functionality of docker offers an enormous amount of flexibility for running programs.
* Usage: ENV key value
* Example: ENV SERVER_WORKS 4

#### EXPOSE
* The EXPOSE command is used to associate a specified port to enable networking between the running process inside the container and the outside world (i.e. the host).
* Usage: EXPOSE [port]
* Example: EXPOSE 8080

#### FROM
* It defines the base image to use to start the build process.
* It can be any image, including the ones you have created previously.
* If a FROM image is not found on the host, docker will try to find it (and download) from the docker image index.
* It needs to be the first command declared inside a Dockerfile.
* Usage: FROM [imagename]
* Example: FROM ubuntu

#### RUN
* The RUN command is the central executing directive for Dockerfiles.
* It takes a command as its argument and runs it to form the image.
* Unlike CMD, it actually is used to build the image (forming another layer on top of the previous one which is committed).
* Usage: RUN [command]
* Example: RUN aptitude install -y riak

#### USER
* The USER directive is used to set the UID (or username) which is to run the container based on the image being built.
* Usage: USER [UID]
* Example: USER 751

#### VOLUME
* The VOLUME command is used to enable access from your container to a directory on the host machine (i.e. mounting it).
* Usage: VOLUME ["/dir_1", "/dir_2" ..]
* Example: VOLUME ["/my_files"]

#### WORKDIR
* The WORKDIR directive is used to set where the command defined with CMD is to be executed.
* Usage: WORKDIR /path
* Example: WORKDIR ~/

#### MAINTAINER
* MAINTAINER Obulapathi N Challa
