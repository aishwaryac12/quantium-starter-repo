#!/usr/bin/bash

python -m pytest dash_modified_visualiser.py

PYTEST_EXIT_CODE=$?

if [ $PYTEST_EXIT_CODE -eq 0 ]
then
  exit 0
else
  exit 1
fi