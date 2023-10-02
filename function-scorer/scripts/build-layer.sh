#!/bin/bash

set -eo pipefail
rm -rf ./function-scorer/package
pip3 install --target ./function-scorer/package/python -r ./function-scorer/requirements.txt