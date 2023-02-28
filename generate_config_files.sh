#!/bin/bash

if [[ $PWD != *"alfred_build" ]]; then
    cd alfred_build
fi

# Build containers
cd config_files
python3 config_files.py
cd ..