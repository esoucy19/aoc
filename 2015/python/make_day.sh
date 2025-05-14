#!/usr/bin/env bash

day="day${1}"

mkdir "$day"
touch "$day"/"$day"{.py,_test.py} "$day"/input.txt
