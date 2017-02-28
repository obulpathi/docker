FROM ubuntu:16.04

MAINTAINER Obul <obulpathi@google.com>

# Update the system
RUN apt-get update
RUN apt-get --yes upgrade

# Install dependencies
RUN apt-get install --yes python-pip python-dev

# Install NumPy and TensorFlow
RUN pip install numpy tensorflow

# Copy the code
RUN mkdir -p /code
COPY code /code
WORKDIR /code

CMD ["/bin/bash"]
