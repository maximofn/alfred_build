#!/bin/bash

# Build ubuntu 20.04 docker image
cd alfred_build
docker build -f docker/Dockerfile.ubuntu_test -t maximofn/ubuntu_20_04_test:0.0.1 ../
# Check if alfred is well installed
alfred_ubuntu=$(docker run -it --rm maximofn/ubuntu_20_04_test:0.0.1 /usr/src/alfred/alfred.py)
if [[ $alfred_ubuntu == *"You need to set your OpenAI API key in the OPENAI_API_KEY environment variable"* ]]; then
    echo -e "\033[0;32mAlfred is well installed in ubuntu 20.04\033[0m"     # Green
else
    echo -e "\033[0;31mAlfred is not well installed in ubuntu 20.04\033[0m" # Red
fi