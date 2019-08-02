#!/bin/bash
echo "Setting flask environment variable..."
export FLASK_APP=/home/jonathan/minionPi/modules/minionAPI.py
echo "Starting API service..."
python3 -m flask run --host=0.0.0.0
