#!/bin/bash

# Build ubuntu 20.04 docker image
rm debian/alfredv1_3.deb
docker build -f docker/Dockerfile.ubuntu_build -t maximofn/ubuntu_20_04_build:0.0.1 ../
docker run -it --rm -v ./debian/:/mnt maximofn/ubuntu_20_04_build:0.0.1 cp /home/alfredv1_3.deb /mnt

# Build fedora 36 docker image
rm fedora/alfred-1.3-1.fc36.x86_64.rpm
docker build -f docker/Dockerfile.fedora_build -t maximofn/fedora36_build:0.0.1 ../
docker run -it --rm -v ./fedora/:/mnt maximofn/fedora36_build:0.0.1 cp /root/rpmbuild/RPMS/x86_64/alfred-1.3-1.fc36.x86_64.rpm /mnt