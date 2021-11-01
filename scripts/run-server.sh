#!/bin/bash

# install pip
pip install -U pip

# installing requirements
pip install -r requirements.txt

# migrate and collect static 
src/manage.py migrate && src/manage.py collectstatic --no-input

echo "Run Django"
src/manage.py runserver 0.0.0.0:8000
echo "Django Killed"