#!/bin/sh

mkdir output 

flake8 --output-file=output/flake8-output.log ../server

export PYTHONPATH=../server
pytest > output/pytest-output.log