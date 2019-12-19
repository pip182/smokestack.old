#!/bin/bash

WORK_DIR="$(dirname "$0")"
PROJECT_DIR="../"

echo "Make sure you have the virtual environment activated... if not please exit now and activate it."
read -p "Press enter to continue or CTRL+C to bail."

sudo apt install build-essential gettext python3-dev zlib1g-dev libpq-dev libtiff5-dev libjpeg8-dev libfreetype6-dev liblcms2-dev libwebp-dev libgraphviz-dev
pip install -r ..//requirements/local.txt
cp env.example ..//.env
