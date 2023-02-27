#!/bin/bash

# Build ubuntu 20.04 docker image
cd alfred_build
docker build -f docker/Dockerfile.ubuntu_test -t maximofn/ubuntu_20_04_test:0.0.1 ../
docker run -it --rm maximofn/ubuntu_20_04_test:0.0.1 /usr/src/alfred/alfred.py