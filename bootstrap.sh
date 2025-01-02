#!/bin/sh
export FLASK_APP=./cashman/index.py
flask run --debug -h 0.0.0.0
