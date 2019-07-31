#!/bin/bash

cd /nfs/git/minionPi/modules
echo "Starting Python virtual environment..."
source /home/jonathan/.local/share/virtualenvs/modules-dJB0a20o/bin/activate
echo "Setting flask environment variable..."
export FLASK_APP=/nfs/git/minionPi/modules/minionAPI.py
echo "Starting API service..."
flask run --host=0.0.0.0
