#!/bin/sh
source .venv/bin/activate
python -m flask --app main run -p $PORT -h 0.0.0.0 --debug