#!/bin/bash

# Install dependencies
pip3 install -r requirements.txt

# Make migrations
python3 manage.py makemigrations --noinput 
python3 manage.py migrate --noinput 
python3 manage.py collectstatic --noinput --clear
