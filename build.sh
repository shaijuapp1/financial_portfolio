#!/bin/bash
# Install dependencies
pip3 install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput

# Apply database migrations
python3 manage.py migrate


