#!/bin/bash

cd "$(dirname "$0")/engine" || exit

python3 parser.py
