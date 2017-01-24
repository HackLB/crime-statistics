#!/usr/bin/env bash

dtstamp=$(date +%Y%m%d_%H%M%S)
. ~/.virtualenvs/crime-statistics/bin/activate

git pull
./cases.py
./crimereports.py
git add -A
git commit -m "$dtstamp"
git push

deactivate