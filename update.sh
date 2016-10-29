#!/usr/bin/env bash

dtstamp = $(date +%Y%m%d_%H%M%S)

workon crime-statistics
git pull
./cases.py
git add -A
git commit -m "$dtstamp"
git push