#!/bin/bash

ALFRED_MESSAGE="Enter your OpenAI API key"

# Build images
docker build -f docker/Dockerfile.ubuntu_test1 -t maximofn/ubuntu_20_04_test1:0.0.1 ../
docker build -f docker/Dockerfile.ubuntu_test2 -t maximofn/ubuntu_20_04_test2:0.0.1 ../
docker build -f docker/Dockerfile.ubuntu_test3 -t maximofn/ubuntu_20_04_test3:0.0.1 ../
docker build -f docker/Dockerfile.fedora_test1 -t maximofn/fedora36_test1:0.0.1 ../
docker build -f docker/Dockerfile.fedora_test2 -t maximofn/fedora36_test2:0.0.1 ../
docker build -f docker/Dockerfile.fedora_test3 -t maximofn/fedora36_test3:0.0.1 ../

# Test ubuntu 20.04 test 1 docker image
alfred_ubuntu=$(echo API_KEY | docker run -i --rm maximofn/ubuntu_20_04_test1:0.0.1 /usr/src/alfred/alfred.py)
if [[ $alfred_ubuntu == *$ALFRED_MESSAGE* ]]; then
    echo -e "\033[0;32mAlfred is well installed in ubuntu 20.04 test 1\033[0m"     # Green
else
    echo -e "\033[0;31mAlfred is not well installed in ubuntu 20.04 test 1\033[0m" # Red
fi

# Test ubuntu 20.04 test 2 docker image
alfred_ubuntu=$(echo API_KEY | docker run -i --rm maximofn/ubuntu_20_04_test1:0.0.1 /usr/src/alfred/alfred.py)
if [[ $alfred_ubuntu == *$ALFRED_MESSAGE* ]]; then
    echo -e "\033[0;32mAlfred is well installed in ubuntu 20.04 test 2\033[0m"     # Green
else
    echo -e "\033[0;31mAlfred is not well installed in ubuntu 20.04 test 2\033[0m" # Red
fi

# Test ubuntu 20.04 test 3 docker image
alfred_ubuntu=$(echo API_KEY | docker run -i --rm maximofn/ubuntu_20_04_test1:0.0.1 /usr/src/alfred/alfred.py)
if [[ $alfred_ubuntu == *$ALFRED_MESSAGE* ]]; then
    echo -e "\033[0;32mAlfred is well installed in ubuntu 20.04 test 3\033[0m"     # Green
else
    echo -e "\033[0;31mAlfred is not well installed in ubuntu 20.04 test 3\033[0m" # Red
fi

# Test fedora 36 test 1 docker image
alfred_ubuntu=$(echo API_KEY | docker run -i --rm maximofn/fedora36_test1:0.0.1 /usr/src/alfred/alfred.py)
if [[ $alfred_ubuntu == *$ALFRED_MESSAGE* ]]; then
    echo -e "\033[0;32mAlfred is well installed in fedora 33 test 1\033[0m"     # Green
else
    echo -e "\033[0;31mAlfred is not well installed in fedora 33 test 1\033[0m" # Red
fi

# Test fedora 36 test 2 docker image
alfred_ubuntu=$(echo API_KEY | docker run -i --rm maximofn/fedora36_test2:0.0.1 /usr/src/alfred/alfred.py)
if [[ $alfred_ubuntu == *$ALFRED_MESSAGE* ]]; then
    echo -e "\033[0;32mAlfred is well installed in fedora 33 test 2\033[0m"     # Green
else
    echo -e "\033[0;31mAlfred is not well installed in fedora 33 test 2\033[0m" # Red
fi

# Test fedora 36 test 3 docker image
alfred_ubuntu=$(echo API_KEY | docker run -i --rm maximofn/fedora36_test3:0.0.1 /usr/src/alfred/alfred.py)
if [[ $alfred_ubuntu == *$ALFRED_MESSAGE* ]]; then
    echo -e "\033[0;32mAlfred is well installed in fedora 33 test 3\033[0m"     # Green
else
    echo -e "\033[0;31mAlfred is not well installed in fedora 33 test 3\033[0m" # Red
fi

# Remove images
docker image rm maximofn/ubuntu_20_04_test1:0.0.1
docker image rm maximofn/ubuntu_20_04_test2:0.0.1
docker image rm maximofn/ubuntu_20_04_test3:0.0.1
docker image rm maximofn/fedora36_test1:0.0.1
docker image rm maximofn/fedora36_test2:0.0.1
docker image rm maximofn/fedora36_test3:0.0.1