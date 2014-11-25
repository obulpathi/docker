FROM          ubuntu:latest
MAINTAINER    Obulpathi N Challa<obulpathi@gmail.com>

RUN           apt-get update && apt-get install -y redis-server
EXPOSE        6379
ENTRYPOINT    ["/usr/bin/redis-server"]
