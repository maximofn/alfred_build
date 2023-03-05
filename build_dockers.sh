#!/bin/bash

# Build ubuntu 20.04 docker image
rm debian/alfredv1_3.deb
docker build -f docker/Dockerfile.ubuntu_build -t maximofn/ubuntu_20_04_build:0.0.1 ../
docker run -it --rm -v ./debian/:/mnt maximofn/ubuntu_20_04_build:0.0.1 cp /home/alfredv1_3.deb /mnt