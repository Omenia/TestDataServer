#!/bin/sh

flake8 --output-file=tests/output/flake8-output.log ../server

export PYTHONPATH=../server
pytest > tests/output/pytest-output.log