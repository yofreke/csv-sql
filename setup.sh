#!/bin/bash
set -e

virtualenv env

. env/bin/activate

pip install -r requirements.txt
pip install -e lib/sqlformatter/
