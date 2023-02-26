#!/bin/bash

# Build ubuntu 20.04 docker image
cd alfred_build
rm ubuntu20.04/alfred.deb
docker build -f docker/Dockerfile.ubuntu -t maximofn/ubuntu_20_04:0.0.1 ../
docker run -it --rm -v ./ubuntu20.04/:/mnt maximofn/ubuntu_20_04:0.0.1 cp /home/alfred.deb /mnt

# Execute docker compose build
# docker compose -f docker/docker-compose-build.yml up